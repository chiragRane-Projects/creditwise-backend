import joblib
import numpy as np
import os

model_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "ml", "credit_model.pkl")
)
model_path = os.path.abspath(model_path)

if not os.path.exists(model_path):
    raise FileNotFoundError(f"credit_model.pkl not found at: {model_path}")

model = joblib.load(model_path)

def predict_credit_score(features: dict) -> dict:
    try:
        income = features["monthly_income"]
        expense = features["monthly_expense"]
        savings_rate = features["savings_rate"]
        emi_count = features["emi_count"]
        tx_count = features["transaction_count"]
    except KeyError as e:
        raise ValueError(f"Missing feature: {e}")

    score = 750
    score -= emi_count * 5
    score += int(savings_rate * 100)
    score = min(850, max(300, score)) 

    creditworthy = score >= 700
    confidence = round((score - 300) / 550, 2)

    return {
        "creditworthy": creditworthy,
        "confidence": confidence
    }

