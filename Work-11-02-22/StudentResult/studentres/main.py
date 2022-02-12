import csv
from fastapi import FastAPI, Depends, File, UploadFile

from .schemas import Student
from sqlalchemy.orm import Session
from .utils import get_db
from .service import service_insert, service_retrive, service_retrive_one, service_delete, service_update, \
    service_read_all_csv, service_read_id_csv, service_insert_record
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

@app.put('/update/{id}')
def updateData(id,stu : Student,db : Session = Depends(get_db)):
    update_data = db.query(models.Student_model).filter(models.Student_model.chance_given == "Yes", models.Student_model.sid == id).all()
    print(update_data)
    for each in update_data:
        print(each)
        new_update = each
        if each.Maths < 75:
            new_update.Maths = stu.Maths
        if each.History < 75:
            new_update.History = stu.History
        if each.Geography < 75:
            new_update.Geography = stu.Geography
        if each.English < 75:
            new_update.English = stu.English
        if each.Civics < 75:
            new_update.Civics = stu.Civics
        if each.Economics < 75:
            new_update.Economics = stu.Economics
    return service_update(new_update,id,db)

@app.get('/readCSVall')
def readCSVData():
    return service_read_all_csv()


@app.get('/readCSV/{id}')
def readCSVDataid(id):
    return service_read_id_csv(id)

@app.post('/upload')
def uploadCSV(data_file: UploadFile = File(...), db : Session = Depends(get_db)):
    print(data_file.filename)
    print(data_file)
    rows = []
    filename = 'C:\\Users\\Admin\\Desktop\\' + data_file.filename
    with open(filename,'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        print(rows)

    return service_insert_record(rows, db)


