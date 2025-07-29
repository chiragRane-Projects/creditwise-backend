import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

np.random.seed(42)
data = {
    "monthly_income": np.random.normal(50000, 15000, 1000).clip(10000, 150000),
    "monthly_expense": np.random.normal(30000, 10000, 1000).clip(5000, 100000),
    "savings_rate": np.random.uniform(0, 0.8, 1000),
    "emi_count": np.random.randint(0, 4, 1000),
    "transaction_count": np.random.randint(10, 100, 1000),
}

df = pd.DataFrame(data)

df['creditworthy'] = (
    (df['savings_rate'] > 0.2) 
    &(df["emi_count"] < 2)
    &(df["monthly_income"] > df["monthly_expense"])
).astype(int)

X = df.drop("creditworthy", axis=1)
y = df["creditworthy"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "backend/ml/credit_model.pkl")

print("✅ Model trained and saved to ml/credit_model.pkl")