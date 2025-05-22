
from pydantic import BaseModel

class  person(BaseModel):
    name: str
    age: float
    image: str