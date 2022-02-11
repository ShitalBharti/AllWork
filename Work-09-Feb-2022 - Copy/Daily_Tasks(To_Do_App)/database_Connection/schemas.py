from pydantic import BaseModel

class Task(BaseModel):
    taskName: str
    taskDescription: str