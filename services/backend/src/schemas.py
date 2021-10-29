from typing import List, Optional

from pydantic import BaseModel


class TextBase(BaseModel):
    body: Optional[str] = None


class TextCreate(TextBase):
    pass


class Text(TextBase):
    id: int
    owner_id: int
    is_human_count: int
    is_ai_count: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    texts: List[Text] = []

    class Config:
        orm_mode = True
