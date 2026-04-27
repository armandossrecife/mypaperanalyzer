from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PaperBase(BaseModel):
    original_filename: str

class PaperResponse(PaperBase):
    id: int
    user_id: int
    title: Optional[str] = None
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class PaperDetailResponse(PaperResponse):
    analysis_started_at: Optional[datetime] = None
    analysis_finished_at: Optional[datetime] = None
    error_message: Optional[str] = None
    
    class Config:
        from_attributes = True
