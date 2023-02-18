from sqlalchemy.orm import Session

import models, schemas

def get_user_by_email(db: Session, email: str):
    '''
    This is also used as a validator if the user already exists or not
    '''
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.hashed_password + "notreallyhashed"
    db_user = models.User(email=user.email,
                          hashed_password=fake_hashed_password,
                          firstname=user.firstname,
                          middlename=user.middlename,
                          lastname=user.lastname,
                          phone=user.phone,
                          yoe=user.yoe,
                          country=user.country,
                          state=user.state,
                          city=user.city,
                          addressline1=user.addressline1,
                          addressline2=user.addressline2,
                          pincode=user.pincode,
                          linkedin=user.linkedin,
                          twitter=user.twitter,
                          github=user.github,
                          stackoverflow=user.stackoverflow,
                          jobexperience1=user.jobexperience1,
                          jobexperience2=user.jobexperience2,
                          gender=user.gender
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
