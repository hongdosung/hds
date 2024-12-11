from typing import Union, Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid1, uuid4
from enum import Enum

class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'


class User(BaseModel):
    id: Optional[UUID] = uuid1() # uuid1은 타임스탬프를 기준으로 생성, uuid4은 랜덤 생성 방식 생성
    id2: Optional[UUID] = uuid4() # uuid1은 타임스탬프를 기준으로 생성, uuid4은 랜덤 생성 방식 생성
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
