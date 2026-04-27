from sqlalchemy.orm import Session
from app.services.user_service import get_user_by_email, create_user
from app.core.security import verify_password
from app.core.jwt import create_access_token

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user

def login_for_access_token(db: Session, email: str, password: str):
    user = authenticate_user(db, email, password)
    if not user:
        return None
    access_token = create_access_token(data={"sub": str(user.id), "email": user.email})
    return access_token
