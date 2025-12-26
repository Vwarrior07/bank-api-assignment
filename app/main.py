from fastapi import FastAPI
from app.database import SessionLocal

app = FastAPI(title="Bank API")

@app.get("/")
def root():
    return {"message": "API is running"}
