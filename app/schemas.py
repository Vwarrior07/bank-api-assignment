from pydantic import BaseModel


class BankBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class BranchBase(BaseModel):
    id: int
    ifsc: str
    branch: str
    address: str | None

    class Config:
        orm_mode = True