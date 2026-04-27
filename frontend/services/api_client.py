import requests
from flask import session
from config import Config

def get_headers():
    token = session.get("access_token")
    if token:
        return {"Authorization": f"Bearer {token}"}
    return {}

def register(name, email, password):
    url = f"{Config.BACKEND_API_URL}/auth/register"
    response = requests.post(url, json={"name": name, "email": email, "password": password})
    return response

def login(email, password):
    url = f"{Config.BACKEND_API_URL}/auth/login"
    data = {"username": email, "password": password}
    response = requests.post(url, data=data)
    return response

def get_me():
    url = f"{Config.BACKEND_API_URL}/auth/me"
    response = requests.get(url, headers=get_headers())
    return response

def list_papers():
    url = f"{Config.BACKEND_API_URL}/papers"
    response = requests.get(url, headers=get_headers())
    return response

def upload_paper(file):
    url = f"{Config.BACKEND_API_URL}/papers/upload"
    files = {"file": (file.filename, file.stream, "application/pdf")}
    response = requests.post(url, headers=get_headers(), files=files)
    return response

def get_paper_detail(paper_id):
    url = f"{Config.BACKEND_API_URL}/papers/{paper_id}"
    response = requests.get(url, headers=get_headers())
    return response

def get_analysis_result(paper_id):
    url = f"{Config.BACKEND_API_URL}/analyses/{paper_id}"
    response = requests.get(url, headers=get_headers())
    return response

def download_result(paper_id, type="all"):
    if type == "authors":
        endpoint = f"analyses/{paper_id}/download/authors-summary"
    elif type == "committee":
        endpoint = f"analyses/{paper_id}/download/committee-summary"
    else:
        endpoint = f"analyses/{paper_id}/download/all"
    
    url = f"{Config.BACKEND_API_URL}/{endpoint}"
    response = requests.get(url, headers=get_headers(), stream=True)
    return response

def get_analysis_logs(paper_id):
    url = f"{Config.BACKEND_API_URL}/analyses/{paper_id}/logs"
    response = requests.get(url, headers=get_headers())
    return response
