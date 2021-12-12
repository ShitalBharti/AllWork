
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/home')
async def create_name():
    return {'Hello': 'Shital'}

class Item(BaseModel):
    name : str
    number : str

@app.post('/home/post')
async def post(item: Item):
    new_name = item.name
    new_no = item.name
    return {'name':new_name,'no':new_no}


"""
If more than one application runs on same port Error: Only one usage of socket address
to change port no:
if __name__ == '__main__':
    uvicorn.run(app, port = 5000)
"""

