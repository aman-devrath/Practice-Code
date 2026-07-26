from pydantic import BaseModel, EmailStr
from datetime import datetime

# using pydantic, we create model of the API
class Post(BaseModel):
    title: str                      
    content: str
    # this is an optional field, if not provided, it will be set to True
    published: bool = True

class PostCreate(Post):
    pass

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime # this is a datetime field

    class Config:
        # this will convert the model to a dictionary
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str