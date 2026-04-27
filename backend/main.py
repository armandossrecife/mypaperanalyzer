from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth_routes, paper_routes, analysis_routes
from app.db.database import engine, Base
import os
from dotenv import load_dotenv

load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Paper Review API", version="1.0.0")

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router, prefix="/api")
app.include_router(paper_routes.router, prefix="/api")
app.include_router(analysis_routes.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to Paper Review API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
