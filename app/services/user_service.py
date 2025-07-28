from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.auth import hash_password

def create_user(user_data : UserCreate, db: Session):
    db_user = db.query(User).filter(User.email == user_data.email).first()
    
    if db_user:
        raise ValueError("Email already registered")
    
    new_user = User(
        full_name = user_data.full_name,
        email = user_data.email,
        hashed_password = hash_password(user_data.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user