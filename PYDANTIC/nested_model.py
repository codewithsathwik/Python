from pydantic import BaseModel

class Address(BaseModel):
    street : str
    cross : int
    area : str

class User(BaseModel):
    id : int
    name : str
    address : Address

address = Address(
    street="Dheem",
    cross=50,
    area="ujire"
)

user = User(
    id=101,
    name="Sathwik",
    address=address
)

print(user)