from pydantic import BaseModel, field_validator, model_validator

#Field validator
class User(BaseModel):
    username : str
    @field_validator("username")
    def username_field_validator(cls, st):
        if len(st) < 5:
            raise ValueError("Username length should be more")
        return st
    

#model validator
class Register(BaseModel):
    password : str
    confirm_password : str
    @model_validator(mode="after")
    def check_password(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password Not matched")
        return values
    

