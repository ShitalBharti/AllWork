from fastapi import HTTPException, status

from .database import SessionLocal
from studentres import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def insert_marks(new_student,db):
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return 'Student Result inserted successfully'

def database_retrive(db):
    user_data = db.query(models.Student_model).all()
    return user_data

def database_retrive_one(id,db):
    single_result = db.query(models.Student_model).filter(models.Student_model.sid == id).first()
    if not single_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data with id {} not present".format(id))
    else:
        return single_result

def database_delete(id,db):
    single_result = db.query(models.Student_model).filter(models.Student_model.sid == id).delete(synchronize_session=False)
    if not single_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data with id {} not present".format(id))
    else:
        db.commit()
        return 'Delete success'

def database_update(update_student,id,db):
    if db.query(models.Student_model).filter(models.Student_model.sid == id).first():
        db.add(update_student)
        db.commit()
        db.refresh(update_student)
        return 'Student Result updated successfully'






