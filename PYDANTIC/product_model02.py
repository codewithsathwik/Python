from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock: bool = True

product_one = Product(id=101, name="Laptop", price="99.5", in_stock=True)

product_two = Product(id=2, name="Mouse", price="9.5")

#always use type anotation