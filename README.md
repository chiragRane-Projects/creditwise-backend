# 💳 CreditWise - AI-Powered Credit Risk & Loan Approval System

CreditWise is an AI-powered backend service that helps fintech apps assess creditworthiness and approve/reject loan applications based on real financial behavior. Built with **FastAPI**, **PostgreSQL**, and a trained **machine learning model**, it allows users to register, upload financial data, and get instant credit scores and application results.

---

## 🚀 Features

* 🔐 **JWT Auth System** – Secure user registration & login
* 📥 **CSV Upload** – Upload transaction data for ML analysis
* 🧠 **Credit Scoring ML Model** – Predicts creditworthiness with real features
* 📊 **Feature Engineering** – Extracts monthly income, expense, savings rate, EMI count, etc.
* 📝 **Loan Application Submission** – Stores prediction + user request in DB
* 🧾 **Built with FastAPI** – Ultra-fast Python backend

---

## 🧠 Machine Learning (Overview)

* **Model:** Logistic Regression
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
creditwise/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── utils/
├── ml/
│   ├── train_model.ipynb  # ML training logic
│   └── credit_model.pkl   # Trained model
├── requirements.txt
├── main.py
├── README.md
```

---

## 📦 Setup

```bash
git clone https://github.com/yourusername/creditwise
cd creditwise
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

PostgreSQL connection string must be configured in `.env` or `core/database.py`.

---

## 🔐 Authentication

* `POST /auth/register` – Register new user
* `POST /auth/login` – Get JWT access token

Include token in headers:

```
Authorization: Bearer <your-token>
```

---

## 🧾 API Endpoints

* `POST /loan/apply` – Apply for a loan using financial features
* `GET /loan/me` – (Optional) View your applications

---

## 🤖 ML Prediction Example

**Input**

```json
{
  "requested_amount": 50000,
  "monthly_income": 60000,
  "monthly_expense": 20000,
  "savings_rate": 0.33,
  "emi_count": 1,
  "transaction_count": 42
}
```

**Output**

```json
{
  "application_id": 2,
  "creditworthy": true,
  "confidence": 0.88,
  "status": "pending"
}
```

---

## 📈 Tech Stack

* **FastAPI** (Python Web Framework)
* **PostgreSQL** (Relational Database)
* **SQLAlchemy** (ORM)
* **Pydantic** (Validation)
* **scikit-learn** (ML)
* **Pandas, NumPy** (Data)

---

## 🧠 Author

**Chirag** – Data Science + BCA student, project-based learner, Linux user, and future AI/Fintech pro.

> Made with ❤️ for real-world ML + API learning.
