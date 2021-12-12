from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas,models
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

@app.post('/blog', status_code = 201)  # /(slash) is home route
async def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog', status_code = status.HTTP_201_CREATED)
async def all_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code = 200)
async def show(id, response: Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=
                            "Blog with id {} is not available".format(id))
       # response.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail':"Blog with id {} is not available".format(id)}
    return blog

@app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id ==
                                        id).delete(synchronize_session = False)
    db.commit()  # -> for committing the operation
    return 'done'

"""
Status - Codes:->
----------------------
201 - created
200 - OK
202 - Accepted
customer response code - import response from FastAPI - with status code give message
404 - file not found
HTTPException - with status code give message
"""
