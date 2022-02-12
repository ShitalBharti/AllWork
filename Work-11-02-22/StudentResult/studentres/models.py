from .database import Base
from sqlalchemy import Column, Integer, String, Float


class Student_model(Base):
    __tablename__ = 'Student_Result'

    sid = Column(Integer,primary_key=True)
    sname = Column(String(30))
    Maths = Column(Float)
    History = Column(Float)
    Geography = Column(Float)
    English = Column(Float)
    Civics = Column(Float)
    Economics = Column(Float)
    status = Column(String(50))
    chance_given = Column(String(10))


