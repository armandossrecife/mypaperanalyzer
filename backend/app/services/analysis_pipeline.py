import os
import json
from datetime import datetime
from sqlalchemy.orm import Session
from app.db.models import Paper, AnalysisResult
from app.services.file_service import create_user_output_directory, save_text_output
from app.services.skill_service import load_skill1, load_skill2
from app.services.openai_service import (
    upload_file_to_openai, 
    generate_paper_summary, 
    generate_follow_up, 
    summarize_text
)
from app.core.config import settings

def run_openai_analysis_pipeline(db: Session, user_id: int, paper_id: int):
    paper = db.query(Paper).filter(Paper.id == paper_id, Paper.user_id == user_id).first()
    if not paper:
        return
    
    try:
        # 3. Update status to processing
        paper.status = "processing"
        paper.analysis_started_at = datetime.now()
        db.commit()
        
        # 4 & 5. Load skills
        skill1 = load_skill1()
        skill2 = load_skill2()
        
        # 7. Upload PDF to OpenAI & Create Vector Store
        openai_file_id, vector_store_id = upload_file_to_openai(db, user_id, paper_id, paper.file_path)
        paper.openai_file_id = openai_file_id
        paper.openai_vector_store_id = vector_store_id
        db.commit()
        
        # 9. Generate Paper_Summary.txt
        summary_prompt = """Você é um avaliador técnico-científico experiente.
Leia cuidadosamente o arquivo PDF anexado, que contém um paper científico.
Produza um resumo técnico preliminar contendo:
1. Tema central do artigo.
2. Objetivo principal.
3. Problema de pesquisa.
4. Hipótese, questão de pesquisa ou motivação.
5. Metodologia utilizada.
6. Dados, corpus, participantes ou artefatos analisados.
7. Técnicas, ferramentas ou modelos utilizados.
8. Principais resultados.
9. Contribuições declaradas.
10. Limitações reconhecidas pelos autores.
11. Pontos mais importantes do trabalho.
Use linguagem técnica, objetiva e estruturada."""
        
        paper_summary, thread_id = generate_paper_summary(db, user_id, paper_id, vector_store_id, summary_prompt)
        
        # 10. Generate Comments to Authors.txt
        authors_prompt = f"""Você é um revisor técnico-científico de uma conferência ou periódico.
Considere o resumo preliminar abaixo.
Também siga rigorosamente as instruções da skill1.md anexada como contexto.
Sua tarefa é produzir comentários técnicos, críticos e construtivos destinados aos autores do artigo.
RESUMO PRELIMINAR:
{paper_summary}
SKILL1 CONTENT:
{skill1}"""
        
        comments_authors = generate_follow_up(db, user_id, paper_id, thread_id, authors_prompt, "2. Comments to Authors")
        
        # 11. Generate Comments to Committee.txt
        committee_prompt = f"""Você é um avaliador sênior escrevendo comentários confidenciais para o comitê do programa.
Considere o resumo preliminar do paper e os comentários preparados para os autores.
Siga rigorosamente as instruções da skill2.md anexada como contexto.
Sua tarefa é produzir comentários técnicos, críticos e confidenciais ao comitê.
RESUMO PRELIMINAR:
{paper_summary}
COMENTÁRIOS PARA OS AUTORES:
{comments_authors}
SKILL2 CONTENT:
{skill2}"""
        
        comments_committee = generate_follow_up(db, user_id, paper_id, thread_id, committee_prompt, "3. Comments to Committee")
        
        # 12 & 13. Generate summaries
        summ_authors_prompt = "Resuma o conteúdo abaixo para no máximo 5000 caracteres. Preserve os pontos mais importantes da avaliação aos autores. Mantenha tom técnico e construtivo."
        authors_summary = summarize_text(db, user_id, paper_id, comments_authors, "4. Authors Review Summary", summ_authors_prompt)
        
        summ_committee_prompt = "Resuma o conteúdo abaixo para no máximo 5000 caracteres. Preserve os pontos mais relevantes para decisão editorial. Mantenha o caráter confidencial."
        committee_summary = summarize_text(db, user_id, paper_id, comments_committee, "5. Committee Review Summary", summ_committee_prompt)
        
        # 15. Save files
        output_dir = create_user_output_directory(user_id, paper_id)
        path_summary = save_text_output(output_dir, "Paper_Summary.txt", paper_summary)
        path_authors = save_text_output(output_dir, "Comments to Authors.txt", comments_authors)
        path_committee = save_text_output(output_dir, "Comments to Committee.txt", comments_committee)
        path_authors_summary = save_text_output(output_dir, "Comments to Authors - Summary 5000 chars.txt", authors_summary)
        path_committee_summary = save_text_output(output_dir, "Comments to Committee - Summary 5000 chars.txt", committee_summary)
        
        # 16. Persist results
        result = AnalysisResult(
            user_id=user_id,
            paper_id=paper_id,
            paper_summary_path=path_summary,
            comments_authors_path=path_authors,
            comments_committee_path=path_committee,
            comments_authors_summary_path=path_authors_summary,
            comments_committee_summary_path=path_committee_summary,
            comments_authors_summary_text=authors_summary,
            comments_committee_summary_text=committee_summary,
            model_used=settings.OPENAI_MODEL
        )
        db.add(result)
        
        # 17. Update status to completed
        paper.status = "completed"
        paper.analysis_finished_at = datetime.now()
        db.commit()
        
    except Exception as e:
        db.rollback()
        paper.status = "failed"
        paper.error_message = str(e)
        paper.analysis_finished_at = datetime.now()
        db.commit()
        print(f"Pipeline failed for paper {paper_id}: {str(e)}")
