from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Branch
from app.schemas import BranchBase

router = APIRouter(prefix="/branches", tags=["Branches"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{ifsc}", response_model=BranchBase)
def get_branch_by_ifsc(ifsc: str, db: Session = Depends(get_db)):
    branch = db.query(Branch).filter(Branch.ifsc == ifsc).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    return branch
