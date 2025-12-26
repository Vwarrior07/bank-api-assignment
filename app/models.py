from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Bank(Base):
    __tablename__ = "banks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    branches = relationship("Branch", back_populates="bank")


class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    ifsc = Column(String, unique=True, nullable=False, index=True)
    branch = Column(String, nullable=False)
    address = Column(String, nullable=True)

    bank_id = Column(Integer, ForeignKey("banks.id"))

    bank = relationship("Bank", back_populates="branches")
