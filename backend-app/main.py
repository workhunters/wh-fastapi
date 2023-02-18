from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/jobs/", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    '''
    In jobs, I will be just pushing the code to the DB, it is on FE to filter it out
    '''
    return crud.create_job(db=db, job=job)

@app.get("/jobs/")
def get_total_jobs(db: Session = Depends(get_db)):
    return crud.get_total_jobs(db=db)

@app.post("/companies/", response_model=schemas.CompanyCreate)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    '''
    Create companies as they are an independent entities
    '''
    return crud.create_company(db=db, company=company)

@app.get("/companies/")
def show_company(db: Session = Depends(get_db)):
    return crud.get_total_companies(db=db)