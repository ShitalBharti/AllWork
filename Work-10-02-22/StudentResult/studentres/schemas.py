from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
   # sid: int
    sname: str
    Maths: Optional[float] = None
    History: Optional[float] = None
    Geography: Optional[float] = None
    English: Optional[float] = None
    Civics: Optional[float] = None
    Economics: Optional[float] = None
    #status: Optional[str] = None
    #chance_given: Optional[str] = None



