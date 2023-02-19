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


class JobBase(BaseModel):
    title: str
    dateposted: Optional[str]

class JobCreate(JobBase):
    location: str
    from_:str
    benefits: str
    bkeyword: str
    qualifications: str
    qkeyword: str
    responsibilities: str
    rkeyword: str
    thumbnail: str
    applylink: str

class Job(JobBase):
    id: int
    companyid: int
    class Config:
        orm_mode=True

class CompanyBase(BaseModel):
    name: str

class CompanyCreate(CompanyBase):
    name: str
    class Config:
        orm_mode=True

class CompanyShow(CompanyBase):
    name: str
    class Config:
        orm_mode=True

class Company(CompanyBase):
    id: int
    class Config:
        orm_mode=True

