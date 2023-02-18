from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: Optional[str]
    email: str

class UserCreate(UserBase):
    hashed_password: str
    firstname: str
    lastname: str
    middlename: str
    yoe: int
    phone: str
    country: str
    state: str
    city: str
    addressline1: str
    addressline2: str
    pincode: str
    linkedin: str
    twitter: str
    github: str
    stackoverflow: str
    jobexperience1: str
    jobexperience2: str
    gender: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode=True

