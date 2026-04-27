import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "change_this_frontend_secret")
    BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://localhost:8000/api")
