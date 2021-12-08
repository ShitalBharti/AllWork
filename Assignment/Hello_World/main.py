
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#get method
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/home")
def write_home():
    return {
        "Name":"Shital",
        "Age":25
    }
@app.get("/welcome")
def write_name():
    return "Hello World Harsha"

@app.get("/home/{user_name}")
def write_username(user_name: str):
    return {
        "Name": user_name,
        "Age" : 25
    }

@app.get("/home2/{age}")
def write_age(age: int):
    return {
        "Id" : 123,
        "Age" : age
    }

# Query handling
@app.get("/home3/{msg}")
def write_age(msg: str , query):
    return {
        "Message" : msg,
        "query": query
    }

list_username = list()
@app.put("/username/{user_name}")
def put_data(user_name:str):
    print(user_name)
    list_username.append(user_name)
    return {
        "username":user_name
    }

@app.post("/postData")
def post_data(user_name: str):
    list_username.append(user_name)
    return {
        "username": list_username
    }

@app.delete("/deleteData/{user_name}")
def delete_data(user_name : str):
    list_username.remove(user_name)
    return {
        "username": list_username
    }

@app.api_route("/homeData",methods=["GET","POST","PUT","DELETE"])
def handle_homeData(username:str):
    print(username)
    return {
        "username":username
    }

# uvicorn main:app --reload  -> Server command to run the application
# Data Validation - Pydantic Module

class NameValues(BaseModel):
    name : str
    country : str
    age : int
    salary : float

@app.post("/pydanticModule")
def post_values(name_value : NameValues):
    print(name_value)
    return {
        "name":name_value.name
    }