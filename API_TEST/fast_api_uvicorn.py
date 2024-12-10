
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from uuid import UUID, uuid1, uuid4

app = FastAPI() # 인스턴스 생성

class Item(BaseModel):
    id: Optional[UUID] = uuid1() # uuid1은 타임스탬프를 기준으로 생성, uuid4은 랜덤 생성 방식 생성
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/src") # get method로 '/'에 해당하는 생성
def read_root():
    return {'Hello': 'World read_root'}

   
@app.get("/src/fast_api/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {'ITEM_ID': item_id, 'q': q}

# 
@app.put("/src/fast_api/{item_id}")
def update_item(item_id: int, item: Item):
    return {'ITEM_ID': item_id, 'ITEM_NAME': item.name, 'ITEM_PRICE': item.price}
    # return {'ITEM_NAME': item.name, 'ITEM_ID': item_id}
