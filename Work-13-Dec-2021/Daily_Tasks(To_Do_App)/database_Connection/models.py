from .database import Base
from sqlalchemy import Column,Integer,String

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer,primary_key=True,index = True)
    task_name = Column(String)
    task_description = Column(String)