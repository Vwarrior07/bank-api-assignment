from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Bank
from app.schemas import BankBase

router = APIRouter(prefix="/banks", tags=["Banks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[BankBase])
def get_banks(db: Session = Depends(get_db)):
    return db.query(Bank).all()
