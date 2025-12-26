from fastapi import FastAPI

from app.database import engine
from app import models

app = FastAPI(title="Bank API")

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API is running"}
