from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    email=Column(String, unique=True, index=True)
    username=Column(String, unique=True)
    firstname=Column(String)
    middlename=Column(String)
    lastname=Column(String)
    phone=Column(String)
    country=Column(String)
    state=Column(String)
    city=Column(String)
    addressline1=Column(String)
    addressline2=Column(String)
    pincode=Column(String)
    yoe=Column(Integer)
    linkedin=Column(String)
    twitter=Column(String)
    github=Column(String)
    stackoverflow=Column(String)
    jobexperience1=Column(String)
    jobexperience2=Column(String)
    gender=Column(String)
    hashed_password=Column(String)
    is_active=Column(Boolean, default=True)


class Job(Base):
    __tablename__="jobs"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    location=Column(String)
    from_=Column(String)
    benefits=Column(String)
    bkeyword=Column(String)
    qualifications=Column(String)
    qkeyword=Column(String)
    responsibilities=Column(String)
    rkeyword=Column(String)
    companyid=Column(Integer,ForeignKey("companies.id"))
    company=relationship("Company", back_populates="jobs")

class Company(Base):
    __tablename__="companies"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, unique=True)

    jobs = relationship("Job", back_populates="company")

