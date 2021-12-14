from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str

"""
@app.post('/blog')
async def create(request: schemas.Blog):
    return request
"""

class ShowBlog(Blog):
    title : str
    body : str
    class Config():  # for response model
        orm_mode = True

class User(BaseModel):
    name : str
    email : str
    password : str