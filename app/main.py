from fastapi import FastAPI

from app.database import engine
from app import models
from app.routers import banks, branches

app = FastAPI(title="Bank API")

models.Base.metadata.create_all(bind=engine)

app.include_router(banks.router)
app.include_router(branches.router)


@app.get("/")
def root():
    return {"message": "API is running"}
