from fastapi import FastAPI

app = FastAPI(title="Bank API")

@app.get("/")
def root():
    return {"message": "API is running"}