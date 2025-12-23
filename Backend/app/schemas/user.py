from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    username:str
    email:EmailStr

class UserCreate(UserBase):
    pass # This inherits username and email from UserBase

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True

