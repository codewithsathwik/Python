from typing import Optional
from pydantic import BaseModel,Field

class Employee(BaseModel):
    id : int
    name : str = Field(
        ...,
        min_length=3,
        max_length=25,
        description="Employee name"
    )
    
    department : Optional[str] = "General"
    salary : float = Field(
        ...,
        ge=20000,    #greater than or equal to
        le=90000,
        description="Salary in INR"
    )