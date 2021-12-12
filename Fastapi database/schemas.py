from fastapi import FastAPI
from pydantic import BaseModel
from . import schemas

app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str

@app.post('/blog')
async def create(request: schemas.Blog):
    return request