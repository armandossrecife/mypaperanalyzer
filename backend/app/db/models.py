from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    papers = relationship("Paper", back_populates="user")
    analysis_results = relationship("AnalysisResult", back_populates="user")
    analysis_logs = relationship("AnalysisLog", back_populates="user")

class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    original_filename = Column(String(255), nullable=False)
    stored_filename = Column(String(255), nullable=False)
    file_path = Column(Text, nullable=False)
    openai_file_id = Column(String(255))
    openai_vector_store_id = Column(String(255))
    title = Column(String(500))
    status = Column(String(50), nullable=False, default="uploaded") # uploaded, processing, completed, failed
    analysis_started_at = Column(DateTime)
    analysis_finished_at = Column(DateTime)
    error_message = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="papers")
    analysis_result = relationship("AnalysisResult", back_populates="paper", uselist=False)
    analysis_logs = relationship("AnalysisLog", back_populates="paper")

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    paper_id = Column(Integer, ForeignKey("papers.id"), nullable=False)
    
    paper_summary_path = Column(Text)
    comments_authors_path = Column(Text)
    comments_committee_path = Column(Text)
    comments_authors_summary_path = Column(Text)
    comments_committee_summary_path = Column(Text)
    
    comments_authors_summary_text = Column(Text)
    comments_committee_summary_text = Column(Text)
    
    model_used = Column(String(100))
    prompt_tokens = Column(Integer)
    completion_tokens = Column(Integer)
    total_tokens = Column(Integer)
    openai_response_metadata = Column(Text) # JSON string
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="analysis_results")
    paper = relationship("Paper", back_populates="analysis_result")

class AnalysisLog(Base):
    __tablename__ = "analysis_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    paper_id = Column(Integer, ForeignKey("papers.id"), nullable=False)
    
    step_name = Column(String(100)) # e.g., "Summary", "Authors Review"
    request_data = Column(Text)
    response_data = Column(Text)
    status = Column(String(50)) # success, error
    error_detail = Column(Text)
    
    created_at = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="analysis_logs")
    paper = relationship("Paper", back_populates="analysis_logs")
