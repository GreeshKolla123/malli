from app.models import User
from app.database import db

def get_users):
    return db.query(User).all()

def create_user(username: str, email: str, password: str):
    user = User(username=username, email=email, password=get_password_hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(id: int):
    return db.query(User).filter(User.id == id).first()