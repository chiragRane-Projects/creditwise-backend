# 💳 CreditWise - AI-Powered Credit Risk System

CreditWise is an AI-powered backend service that helps fintech apps assess creditworthiness based on real financial behavior. Built with **FastAPI**, and a trained **machine learning model**, upload financial data, and get instant credit scores and application results.

---

## 🚀 Features
* 📥 **CSV Upload** – Upload transaction data for ML analysis
* 🧠 **Credit Scoring ML Model** – Predicts creditworthiness with real features
* 📊 **Feature Engineering** – Extracts monthly income, expense, savings rate, EMI count, etc.
* 📝 **Loan Application Submission** – Stores prediction + user request in DB
* 🧾 **Built with FastAPI** – Ultra-fast Python backend

---

## 🧠 Machine Learning (Overview)

* **Model:** RandomForestClassifier
* **Target:** Predict whether a user is creditworthy (1 or 0)
* **Features:**

  * Monthly Income
  * Monthly Expense
  * Savings Rate
  * EMI Count
  * Total Transactions
* **Accuracy:** \~85% on test data

---

## 📂 Project Structure

```
creditwise-backend/
├── app/
│   ├── api/
├── ml/
│   ├── train_model.ipynb  # ML training logic
│   └── credit_model.pkl   # Trained model
├── requirements.txt
├── run.py
├── sample.csv #sample csv file for testing
├── README.md
```

---

## 📦 Setup

```bash
git clone https://github.com/chiragRane-Projects/creditwise-backend
cd creditwise-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

---

## 🧾 API Endpoints

* `POST /api/v1/user/upload-statement` – GET a credit-worthiness as per your financial features
---

## 🤖 ML Prediction Example

**Input**

```file
Input the csv file in the same format as sample.csv in root of the directory
```

**Output**

```json
{
    "message": "Bank Statement parsed successfully",
    "features": {
        "monthly_income": 90000.0,
        "monthly_expense": 43000.0,
        "savings_rate": 0.52,
        "emi_count": 2,
        "transaction_count": 10
    },
    "prediction": {
        "creditworthy": true,
        "confidence": 0.89
    }
}
```

---

## 📈 Tech Stack

* **FastAPI** (Python Web Framework)
* **scikit-learn** (ML)
* **Pandas, NumPy** (Data)
* **NextJS, Tailwind** (Frontend)

---

## 🧠 Author

**Chirag** – Data Science + BCA student, project-based learner, Linux user, and future AI/Fintech pro.

> Made with ❤️ for real-world ML + API learning.
