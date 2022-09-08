from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserUpdate(BaseModel):
    email: EmailStr
    password: str
    new_email: EmailStr
    new_password: str


class UserNew(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True
