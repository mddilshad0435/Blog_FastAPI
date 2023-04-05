from pydantic import BaseModel
from typing import List, Union

class BlogExtend(BaseModel):
    name: str
    body: str
    

class Blog(BlogExtend):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True

class BlogResponse(BaseModel):
    name: str
    body: str
    creator: UserResponse
    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None