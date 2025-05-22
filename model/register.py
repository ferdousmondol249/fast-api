from pydantic import BaseModel


class register_model(BaseModel):
    name:str
    email:str
    password: str