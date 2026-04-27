import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "Paper Review API")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./paper_review.db")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "change_this_secret_key")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
    
    MAX_UPLOAD_SIZE_MB: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", "30"))
    
    STORAGE_DIR: str = os.getenv("STORAGE_DIR", "storage")
    SKILLS_DIR: str = os.getenv("SKILLS_DIR", "storage/skills")
    UPLOADS_DIR: str = os.getenv("UPLOADS_DIR", "storage/uploads")
    OUTPUTS_DIR: str = os.getenv("OUTPUTS_DIR", "storage/outputs")
    TEMP_DIR: str = os.getenv("TEMP_DIR", "storage/temp")
    
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    OPENAI_SUMMARY_MODEL: str = os.getenv("OPENAI_SUMMARY_MODEL", "gpt-4o")
    
    class Config:
        case_sensitive = True

settings = Settings()
