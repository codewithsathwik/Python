# convert pydatic datatype into python dict, json, xml etc..

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class User(BaseModel):
    id: int
    name : str
    email : str
    is_active : bool = True
    createdAt : datetime
    address : Address
    tags : List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v:v.strftime('%d-%M-%Y %H::m:%S')
        }
    )

user = User(
    id=1,
    name="SAthwik",
    email="sathwikms@gmail.com",
    createdAt=datetime(2024,3,15,14,30),
    address=Address(
        street="gowrikalve",
        city="CKM",
        postal_code="577101"
    ),
    is_active=False,
    tags=["sa","fda"]
)

pyhton_dump = user.model_dump()
print(type(pyhton_dump))

python_json_str = user.model_dump_json()
print(python_json_str)
print(type(python_json_str))