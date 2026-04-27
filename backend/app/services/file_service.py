import os
import shutil
from pathlib import Path
from app.core.config import settings

def validate_pdf_file(filename: str):
    return filename.lower().endswith('.pdf')

def create_user_paper_directory(user_id: int, paper_id: int):
    path = Path(settings.UPLOADS_DIR) / f"user_{user_id}" / f"paper_{paper_id}"
    path.mkdir(parents=True, exist_ok=True)
    return str(path)

def create_user_output_directory(user_id: int, paper_id: int):
    path = Path(settings.OUTPUTS_DIR) / f"user_{user_id}" / f"paper_{paper_id}"
    path.mkdir(parents=True, exist_ok=True)
    return str(path)

def save_uploaded_pdf(file_content, destination_path: str):
    with open(destination_path, "wb") as buffer:
        buffer.write(file_content)

def save_text_output(output_dir: str, filename: str, content: str):
    path = Path(output_dir) / filename
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return str(path)

def read_text_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def create_results_zip(output_dir: str):
    # Zip the entire output directory
    zip_path = Path(output_dir).parent / f"{Path(output_dir).name}_results"
    shutil.make_archive(str(zip_path), 'zip', output_dir)
    return f"{zip_path}.zip"
