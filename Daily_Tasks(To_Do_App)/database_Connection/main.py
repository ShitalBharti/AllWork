from fastapi import FastAPI,Depends,HTTPException,status
from . import models, schemas
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/task') # create a task
def createTask(request: schemas.Task, db : Session = Depends(get_db)):
    new_task = models.Task(task_name = request.taskName, task_description = request.taskDescription)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return "Task Created Successfully"

@app.get('/getTask')   # get all tasks
def getTask(db : Session = Depends(get_db)):
    all_task = db.query(models.Task).all()
    return all_task

# first() - used to return the first value of the selected column.
@app.get('/getTask/{id}')
def getTaskById(id,db : Session = Depends(get_db)):
    single_task = db.query(models.Task).filter(models.Task.id == id).first()
    if not single_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task with id {} not present".format(id))
    else:
        return single_task



