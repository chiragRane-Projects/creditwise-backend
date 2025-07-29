from fastapi import APIRouter, HTTPException, File, UploadFile
import pandas as pd
from io import BytesIO
from app.utils.feature_extractor import extract_features
from app.utils.ml_model import predict_credit_score

router = APIRouter()

@router.post("/upload-statement")
def upload_bank_statement(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")
    
    try:
        contents = file.file.read()
        df = pd.read_csv(BytesIO(contents))
        
        if not set(["Date", "Description", "Amount", "Type"]).issubset(df.columns):
            raise HTTPException(status_code=422, detail="Invalid CSV format. Expected columns: Date, Description, Amount, Type.")
        
        features = extract_features(df)
        
        score = predict_credit_score(features)
        
        return{
            "message": "Bank Statement parsed successfully",
            "features": features,
            "prediction": score
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))