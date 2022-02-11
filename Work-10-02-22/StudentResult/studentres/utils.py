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


'''
def database_update(name,id,loc,db):
    update_obj = db.query(Employee_model).filter(Employee_model.eid == id).first()
    update_obj.ename = name
    update_obj.eloc = loc
    db.add(update_obj)
    db.commit()
    db.refresh(update_obj)
    return "data updated successfully"


'''