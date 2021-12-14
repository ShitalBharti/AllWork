from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas,models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext

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

@app.get('/blog', response_model = List[schemas.ShowBlog]) # with response model
async def all_blogs_no_id(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

"""
@app.get('/blog', status_code = status.HTTP_201_CREATED) # without response model
async def all_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
"""

@app.get('/blog/{id}', status_code = 200)  # Without response model
async def show(id, response: Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=
                            "Blog with id {} is not available".format(id))
       # response.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail':"Blog with id {} is not available".format(id)}
    return blog

@app.get('/blog/{id}', status_code = 200,response_model = schemas.ShowBlog) # with response model
async def showBlog(id, response: Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=
                            "Blog with id {} is not available".format(id))
    else:
        return blog

@app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id ==
                                        id).delete(synchronize_session = False)
    db.commit()  # -> for committing the operation
    return 'done'

@app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroyIfPresent(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog with id {} not found'.format(id))
    else:
        blog.delete(synchronize_session = False)
        db.commit()  # -> for committing the operation
        return 'done'

@app.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db:Session = Depends(get_db)):
    # db.query(models.Blog).filter(models.Blog.id == id).update({'title':'updated title'}) # it will update title to updated title
    #db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())  # it will update title to dynamic titles
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Blog with id {} not found'.format(id))
    else:
        blog.update(request.dict())
        db.commit()
        return 'updated successfully'

# New table User:

pwd_cxt = CryptContext(schemes = ["bcrypt"], deprecated = "auto") # -> Encrypt password
@app.post('/user')
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    hashedPassword = pwd_cxt.hash(request.password) # -> Hashing password
    new_user = models.User(name = request.name, email = request.email, password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


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
