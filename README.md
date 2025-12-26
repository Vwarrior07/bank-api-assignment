# Bank API Assignment
A REST API built using **FastAPI** to expose bank and branch information.
The project focuses on clean backend architecture, relational data modeling,
and proper API design.

---

## Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite (easily switchable to PostgreSQL/MySQL)
- Pytest

---

## Features

- Fetch list of all banks
- Fetch branches for a specific bank
- Fetch branch details using IFSC
- Proper 404 handling for invalid inputs
- Automated API tests

---

## API Endpoints
### Get all banks
GET /banks

### Get branches for a bank
GET /banks/{bank_id}/branches

### Get branch by IFSC
GET /branches/{ifsc}

## Project Structure
bank-api-assignment/
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── routers/
│     ├── banks.py
│     └── branches.py
├── scripts/
│ └── load_data.py
├── tests/
│ ├── conftest.py
│ └── test_api.py
├── data/
│ └── bank_branches.csv
├── requirements.txt
└── README.md

---

## Database Design

- **Bank**
  - id (PK)
  - name
- **Branch**
  - id (PK)
  - ifsc (unique)
  - branch
  - address
  - bank_id (FK)

One bank can have multiple branches.

---

## How to Run

### Install dependencies
python -m pip install -r requirements.txt

### Run the server
uvicorn app.main:app --reload

### API Documentation
http://127.0.0.1:8000/docs

### Load Data
python -m scripts.load_data

### Run Tests
pytest

## Development Notes
-Built incrementally with meaningful commits
-Database-agnostic design
-Dataset provided separately as part of the assignment
-No proprietary or company-specific names used