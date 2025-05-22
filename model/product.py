from pydantic import BaseModel
from typing import Optional

class product(BaseModel):
    name:str
    price:float
    in_stock: bool=True





class ProductUpdate(BaseModel):
    name: Optional[str]=None
    price: Optional[float]=None
    in_stock: Optional[bool]=None