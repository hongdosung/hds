############################################################################################
# python 설치:
# - pip3 install fastapi "uvicorn[standard]"
# - pip install pytest
# 서버 실행방법(터미널): uvicorn main:app <= uvicorn 서버는 python에서 제공해주는 API 서버
# 웹 확인
# - http://localhost:8000/API_TEST
# - http://localhost:8000/API_TEST/fast_api/5?q=somequery2
# Swagger 경로: http://localhost:8000/docs
# ReDoc 경로: http://localhost:8000/redoc
# 최초 작성일자: 2024.02.10
############################################################################################

from fastapi import FastAPI
from typing import Union, Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid1, uuid4
from enum import Enum
#from models import User

# class Gender(str, Enum):
#     male = 'male'
#     female = 'female'
#
#
# class Role(str, Enum):
#     admin = 'admin'
#     user = 'user'
#     student = 'student'
#
#
# class User(BaseModel):
#     id: Optional[UUID] = uuid1() # uuid1은 타임스탬프를 기준으로 생성, uuid4은 랜덤 생성 방식 생성
#     id2: Optional[UUID] = uuid4() # uuid1은 타임스탬프를 기준으로 생성, uuid4은 랜덤 생성 방식 생성
#     first_name: str
#     last_name: str
#     middle_name: Optional[str]
#     gender: Gender
#     roles: List[Role]


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


app = FastAPI() # 인스턴스 생성

# db: List[User] = [
#     User(id=uuid4(), first_name='hond', last_name='do sung')
# ]


kk = list()

@app.get("/API_TEST") # get method로 '/'에 해당하는 생성
def read_root():
    return {'Hello': 'World read_root'}


@app.get("/API_TEST/fast_api/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {'item_id': item_id, 'q': q}


@app.put("/API_TEST/fast_api/{item_id}")
def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'ITEM_NAME': item.name, 'ITEM_PRICE': item.price}
    #return {'ITEM_NAME': item.name, 'item_id': item_id}


