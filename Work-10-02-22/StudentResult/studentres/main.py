from typing import List

from fastapi import FastAPI, Depends

from .schemas import Student
from sqlalchemy.orm import Session
from .utils import get_db
from .service import service_insert, service_retrive, service_retrive_one, service_delete
from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/insertdata')
def insert_marks(stu : Student, db : Session = Depends(get_db)):
    new_student = models.Student_model(sname = stu.sname, Maths = stu.Maths, History = stu.History, Geography = stu.Geography, English = stu.English,
                                       Civics = stu.Civics, Economics = stu.Economics)
    print(new_student)
    return service_insert(new_student,db)

@app.get('/retrieve')
def retrieve_data(db : Session = Depends(get_db)):
    return service_retrive(db)

@app.get('/retrieve/{id}')
def getDataById(id,db : Session = Depends(get_db)):
    return service_retrive_one(id,db)

@app.delete('/dataDelete/{id}')
def deleteData(id,db : Session = Depends(get_db)):
    return service_delete(id, db)


'''

@app.get('/retrieve',status_code=200, response_model = List[EmployeeResponse])
def retrieve_data(db : Session = Depends(get_db)):
    return service_retrive(db)

@app.get('/retrieve/{id}',status_code=200, response_model = EmployeeResponse)
def retrieve_data(id:int, db : Session = Depends(get_db)):
    return service_retrive_one(id,db)

@app.put('/update')
def update_data(emp : Employee, db : Session = Depends(get_db)):
    name = emp.ename
    id = emp.eid
    loc = emp.eloc
    return service_update(name,id,loc,db)

if __name__ == '__main__':
    uvicorn.run(app)
'''