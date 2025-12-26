from pydantic import BaseModel


class BankBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True