from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    id : int
    items : List[str]
    quantities : Dict[str,int]

class Blog(BaseModel):
    title : str
    content:str
    url: Optional[str] = None