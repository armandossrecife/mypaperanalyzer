from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import AnalysisResult, Paper, AnalysisLog
from app.schemas.analysis_schema import AnalysisResultResponse, AnalysisLogResponse
from app.api.auth_routes import get_current_user
from app.services.file_service import create_results_zip
from typing import List
import os

router = APIRouter(prefix="/analyses", tags=["analyses"])

@router.get("/{paper_id}", response_model=AnalysisResultResponse)
def get_analysis(paper_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    result = db.query(AnalysisResult).filter(
        AnalysisResult.paper_id == paper_id, 
        AnalysisResult.user_id == current_user.id
    ).first()
    
    if not result:
        # Check if paper exists and its status
        paper = db.query(Paper).filter(Paper.id == paper_id, Paper.user_id == current_user.id).first()
        if not paper:
            raise HTTPException(status_code=404, detail="Paper not found")
        
        return {
            "paper_id": paper_id,
            "status": paper.status,
            "created_at": paper.created_at
        }
    
    return {
        "paper_id": result.paper_id,
        "status": "completed",
        "comments_authors_summary": result.comments_authors_summary_text,
        "comments_committee_summary": result.comments_committee_summary_text,
        "model_used": result.model_used,
        "created_at": result.created_at
    }

@router.get("/{paper_id}/download/authors-summary")
def download_authors_summary(paper_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    result = db.query(AnalysisResult).filter(AnalysisResult.paper_id == paper_id, AnalysisResult.user_id == current_user.id).first()
    if not result or not result.comments_authors_summary_path:
        raise HTTPException(status_code=404, detail="Result not found")
    return FileResponse(result.comments_authors_summary_path, media_type="text/plain", filename="Authors_Summary.txt")

@router.get("/{paper_id}/download/committee-summary")
def download_committee_summary(paper_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    result = db.query(AnalysisResult).filter(AnalysisResult.paper_id == paper_id, AnalysisResult.user_id == current_user.id).first()
    if not result or not result.comments_committee_summary_path:
        raise HTTPException(status_code=404, detail="Result not found")
    return FileResponse(result.comments_committee_summary_path, media_type="text/plain", filename="Committee_Summary.txt")

@router.get("/{paper_id}/download/all")
def download_all_results(paper_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    result = db.query(AnalysisResult).filter(AnalysisResult.paper_id == paper_id, AnalysisResult.user_id == current_user.id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    
    output_dir = os.path.dirname(result.paper_summary_path)
    zip_path = create_results_zip(output_dir)
    
    return FileResponse(zip_path, media_type="application/zip", filename=f"paper_{paper_id}_results.zip")

@router.get("/{paper_id}/logs", response_model=List[AnalysisLogResponse])
def get_analysis_logs(paper_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    logs = db.query(AnalysisLog).filter(
        AnalysisLog.paper_id == paper_id, 
        AnalysisLog.user_id == current_user.id
    ).order_by(AnalysisLog.created_at.asc()).all()
    return logs
