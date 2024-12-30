###############################################################################
# python 설치
# - pip3 install fastapi "uvicorn[standard]"
# - pip install pytest
# 서버 실행방법(터미널)
# - uvicorn main:app --reload <= uvicorn 서버는 python에서 제공해주는 API 서버
# 웹 확인
# - http://localhost:8000/API_TEST
# - http://localhost:8000/API_TEST/fast_api/5?q=somequery2
# Swagger 경로: http://localhost:8000/docs
# ReDoc 경로: http://localhost:8000/redoc
# 최초 작성일자: 2024.02.10
###############################################################################
from http.client import HTTPException

from fastapi import FastAPI, HTTPException
from typing import Union, List
from pydantic import BaseModel
from uuid import UUID, uuid1, uuid4
from models import User, Role, Gender, UserUpdateRequest

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


app = FastAPI()  # 인스턴스 생성

db: List[User] = [
    User(id=uuid1(), id2=uuid4(), first_name='hong01', middle_name='do',
         last_name='sung', gender=Gender.female, roles=[Role.student]),
    User(id=uuid1(), id2=uuid4(), first_name='hong02', middle_name='do',
         last_name='sung', gender=Gender.male, roles=[Role.admin, Role.user])
]


@app.get("/API_TEST")  # get method로 '/'에 해당하는 생성
def read_root():
    return {'Hello': 'World read_root'}


@app.get("/API_TEST/fast_api/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {'item_id': item_id, 'q': q}

@app.get("/API_TEST/v1/users")
async def fetch_user():
    return db

@app.post("/API_TEST/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/API_TEST/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")


@app.put("/API_TEST/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return

    raise HTTPException(status_code=404, detail=f"[update_user] User with id: {user_id} not found")

@app.put("/API_TEST/fast_api/{item_id}")
def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'ITEM_NAME': item.name, 'ITEM_PRICE': item.price}
    #return {'ITEM_NAME': item.name, 'item_id': item_id}

