from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.db.models import Paper
from app.schemas.paper_schema import PaperResponse, PaperDetailResponse
from app.api.auth_routes import get_current_user
from app.services.file_service import validate_pdf_file, create_user_paper_directory, save_uploaded_pdf
from app.services.analysis_pipeline import run_openai_analysis_pipeline
import os
import uuid

router = APIRouter(prefix="/papers", tags=["papers"])

@router.post("/upload", response_model=PaperResponse)
async def upload_paper(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...), 
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    if not validate_pdf_file(file.filename):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # Generate internal filename
    stored_filename = f"{uuid.uuid4().hex}.pdf"
    
    # Create temporary record to get paper_id
    db_paper = Paper(
        user_id=current_user.id,
        original_filename=file.filename,
        stored_filename=stored_filename,
        file_path="TEMP_PATH", # Will update
        status="uploaded"
    )
    db.add(db_paper)
    db.commit()
    db.refresh(db_paper)
    
    # Save file
    paper_dir = create_user_paper_directory(current_user.id, db_paper.id)
    file_path = os.path.join(paper_dir, stored_filename)
    
    content = await file.read()
    save_uploaded_pdf(content, file_path)
    
    db_paper.file_path = file_path
    db.commit()
    
    # Start pipeline in background
    background_tasks.add_task(run_openai_analysis_pipeline, db, current_user.id, db_paper.id)
    
    return db_paper

@router.get("/", response_model=List[PaperResponse])
def list_papers(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(Paper).filter(Paper.user_id == current_user.id).all()

@router.get("/{paper_id}", response_model=PaperDetailResponse)
def get_paper(paper_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    paper = db.query(Paper).filter(Paper.id == paper_id, Paper.user_id == current_user.id).first()
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")
    return paper
