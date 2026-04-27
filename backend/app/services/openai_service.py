import openai
import json
import time
from datetime import datetime
from sqlalchemy.orm import Session
from app.core.config import settings
from app.db.models import AnalysisLog
import os

# Inicialização do cliente
client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

def record_log(db: Session, user_id: int, paper_id: int, step_name: str, request_data: dict, response_data: dict = None, status: str = "success", error_detail: str = None):
    log = AnalysisLog(
        user_id=user_id,
        paper_id=paper_id,
        step_name=step_name,
        request_data=json.dumps(request_data, indent=2, ensure_ascii=False) if request_data else None,
        response_data=json.dumps(response_data, indent=2, ensure_ascii=False) if response_data else None,
        status=status,
        error_detail=error_detail
    )
    db.add(log)
    db.commit()

def create_new_conversation():
    """Cria uma nova conversa/thread."""
    try:
        if hasattr(client, 'conversations'):
            return client.conversations.create().id
        elif hasattr(client, 'beta') and hasattr(client.beta, 'threads'):
            return client.beta.threads.create().id
        return None
    except:
        return None

def get_vector_store_service():
    """Tenta localizar o serviço de Vector Stores no cliente."""
    try:
        if hasattr(client, 'beta') and hasattr(client.beta, 'vector_stores'): return client.beta.vector_stores
        if hasattr(client, 'vector_stores'): return client.vector_stores
    except: pass
    return None

def upload_file_to_openai(db: Session, user_id: int, paper_id: int, file_path: str):
    try:
        # 1. Upload File
        with open(file_path, "rb") as f:
            file_response = client.files.create(file=f, purpose="assistants")
        file_id = file_response.id
        
        vs_service = get_vector_store_service()
        if not vs_service: return file_id, None

        # 2. Create Vector Store
        vector_store = vs_service.create(name=f"VS_Paper_{paper_id}")
        
        # 3. Add file to store
        vs_file = vs_service.files.create(vector_store_id=vector_store.id, file_id=file_id)
        
        # 4. POLLING: Aguardar indexação (até 15 segundos)
        # O modelo precisa que o status seja 'completed' para encontrar conteúdo
        start_time = time.time()
        while time.time() - start_time < 15:
            check = vs_service.files.retrieve(vector_store_id=vector_store.id, file_id=file_id)
            if check.status == "completed":
                record_log(db, user_id, paper_id, "Indexation", {"file_id": file_id}, {"status": "completed", "duration": round(time.time()-start_time, 2)})
                break
            if check.status == "failed":
                raise Exception(f"Falha na indexação do PDF: {check.last_error}")
            time.sleep(1)
        
        return file_id, vector_store.id
    except Exception as e:
        record_log(db, user_id, paper_id, "Upload Fail", {"file_path": file_path}, status="error", error_detail=str(e))
        raise e

def find_conv_id_recursively(obj):
    if isinstance(obj, str): return obj if obj.startswith('conv_') else None
    if isinstance(obj, dict):
        for v in obj.values():
            found = find_conv_id_recursively(v)
            if found: return found
    if hasattr(obj, '__dict__'): return find_conv_id_recursively(obj.__dict__)
    return None

def extract_conversation_id(response):
    for field in ['conversation_id', 'conversation', 'id']:
        val = getattr(response, field, None)
        if val and isinstance(val, str) and val.startswith('conv_'): return val
    return find_conv_id_recursively(response)

def generate_paper_summary(db: Session, user_id: int, paper_id: int, vector_store_id: str, prompt: str):
    step_name = "1. Paper Summary"
    req_data = {"vector_store_id": vector_store_id, "prompt_preview": prompt[:100]}
    try:
        conv_id = create_new_conversation()
        
        # Estrutura exigida pela Responses API do gpt-5-mini
        tools = [{"type": "file_search"}]
        if vector_store_id:
            tools[0]["vector_store_ids"] = [vector_store_id]
        
        response = client.responses.create(
            model=settings.OPENAI_MODEL,
            input=[{"role": "user", "content": prompt}],
            tools=tools,
            conversation=conv_id
        )
        
        res_conv = extract_conversation_id(response) or conv_id
        content = response.output_text if hasattr(response, 'output_text') else response.choices[0].message.content
        
        record_log(db, user_id, paper_id, step_name, req_data, {"conversation": res_conv, "content_preview": content[:200]})
        return content, res_conv
    except Exception as e:
        record_log(db, user_id, paper_id, step_name, req_data, status="error", error_detail=str(e))
        raise e

def generate_follow_up(db: Session, user_id: int, paper_id: int, conversation: str, prompt: str, step_name: str):
    req_data = {"conversation": conversation}
    try:
        response = client.responses.create(
            model=settings.OPENAI_MODEL,
            conversation=conversation,
            input=[{"role": "user", "content": prompt}]
        )
        content = response.output_text if hasattr(response, 'output_text') else response.choices[0].message.content
        record_log(db, user_id, paper_id, step_name, req_data, {"content_preview": content[:200]})
        return content
    except Exception as e:
        record_log(db, user_id, paper_id, step_name, req_data, status="error", error_detail=str(e))
        raise e

def summarize_text(db: Session, user_id: int, paper_id: int, text: str, step_name: str, prompt_template: str):
    full_prompt = f"{prompt_template}\n\nCONTENT:\n{text}"
    try:
        response = client.responses.create(
            model=settings.OPENAI_SUMMARY_MODEL,
            input=[{"role": "user", "content": full_prompt}]
        )
        content = response.output_text if hasattr(response, 'output_text') else response.choices[0].message.content
        record_log(db, user_id, paper_id, step_name, {}, {"response": content[:200]})
        return content
    except Exception as e:
        record_log(db, user_id, paper_id, step_name, {}, status="error", error_detail=str(e))
        raise e
