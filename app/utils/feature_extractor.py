import pandas as pd

def extract_features(df: pd.DataFrame) -> dict:
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)

    credits = df[df['Type'].str.lower() == "credit"]
    debits = df[df['Type'].str.lower() == "debit"]

    monthly_income = credits['Amount'].sum() / max(df['Date'].dt.month.nunique(), 1)
    monthly_expense = abs(debits['Amount'].sum() / max(df['Date'].dt.month.nunique(), 1))

    savings_rate = (monthly_income - monthly_expense) / monthly_income if monthly_income else 0

    emi_keywords = ["emi", "loan", "nbfc", "credit card"]
    emi_flags = df['Description'].str.lower().apply(lambda x: any(keyword in x for keyword in emi_keywords))
    emi_count = emi_flags.sum()

    return {
        "monthly_income": round(float(monthly_income), 2),
        "monthly_expense": round(float(monthly_expense), 2),
        "savings_rate": round(float(savings_rate), 2),
        "emi_count": int(emi_count),
        "transaction_count": int(len(df))
    }
