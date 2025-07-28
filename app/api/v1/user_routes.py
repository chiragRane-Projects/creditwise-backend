from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserOut, UserLogin
from app.services.user_service import create_user
from app.models.user import User
from app.core.auth import get_current_user, verify_password, create_access_token
from app.core.config import settings
import pandas as pd
from io import BytesIO
from app.utils.feature_extractor import extract_features

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(user, db)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.email).first()
    
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    access_token = create_access_token(
        data={"sub": str(user.id), "role": user.user_type},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "user_type": user.user_type
        }
    }

@router.get("/me", response_model=UserOut)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/upload-statement")
def upload_bank_statement(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")
    
    try:
        contents = file.file.read()
        df = pd.read_csv(BytesIO(contents))
        
        if not set(["Date", "Description", "Amount", "Type"]).issubset(df.columns):
            raise HTTPException(status_code=422, detail="Invalid CSV format. Expected columns: Date, Description, Amount, Type.")
        
        features = extract_features(df)
        
        return{
            "message": "Bank Statement parsed successfully",
            "features": features
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))