from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnalysisResultResponse(BaseModel):
    paper_id: int
    status: str
    comments_authors_summary: Optional[str] = None
    comments_committee_summary: Optional[str] = None
    model_used: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class AnalysisLogResponse(BaseModel):
    id: int
    step_name: str
    request_data: Optional[str] = None
    response_data: Optional[str] = None
    status: str
    error_detail: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
        # Adding a custom mapping if field names differ slightly
        # For example, mapping comments_authors_summary_text to comments_authors_summary
