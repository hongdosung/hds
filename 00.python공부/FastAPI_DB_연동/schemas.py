# schemas.py
# Pydantic 모델을 정의

from pydantic import BaseModel
from typing import Optional

# 사용자 데이터 모델 정의
class UserBase(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
