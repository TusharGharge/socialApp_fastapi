from datetime import datetime
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from typing import Optional, List


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    owner_id = int

    # rating: Optional[int] = None


class Postcreate(PostBase):
    pass


class Userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True


class Post(BaseModel):
    id = int
    title: str
    content: str
    published: bool = True
    created_at: datetime
    owner: Userout
    # rating: Optional[int] = None
    class config:
        orm_mode = True


class Usercreate(BaseModel):
    email: EmailStr
    password: str


class Userlogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
