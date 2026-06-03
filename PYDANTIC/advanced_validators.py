from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class User(BaseModel):      
    first_name : str
    last_name : str

    @field_validator("first_name","last_name")
    def name_capitalized(cls, value):
        if value.istitle():
            raise ValueError("Its not capitalized.")
        return value
    
class EmailValid(BaseModel):
    email : str

    @field_validator("email")
    def email_lower(cls, v):
        return v.lower().strip()
    

class Price(BaseModel):
    price : str

    @field_validator("price", mode="before")
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$',''))
        return v
    
class DateRange(BaseModel):
    start_date : datetime
    end_date : datetime

    @model_validator(mode="after")
    def date_validated(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError("Invalid start date")
        return values