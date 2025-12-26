from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Bank
from app.schemas import BankBase

from app.models import Branch
from app.schemas import BranchBase

from fastapi import HTTPException

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


@router.get("/{bank_id}/branches", response_model=list[BranchBase])
def get_branches_for_bank(
    bank_id: int,
    db: Session = Depends(get_db)
):
    branches = db.query(Branch).filter(Branch.bank_id == bank_id).all()

    if not branches:
        raise HTTPException(status_code=404, detail="Bank not found or has no branches")

    return branches