##### FastAPI #####
# FastAPI는 최신 ASGI 표준을 기반으로 한 고성능 웹 프레임워크로, 비동기 처리를 지원하며, 빠른 속도와 높은 생산성을 제공합니다.
# FastAPI는 자동화된 데이터 검증과 문서화 기능을 내장하고 있어, 
# 개발자가 보다 효율적으로 RESTful API를 개발할 수 있도록 도와줍니다.

# FastAPI를 사용한 데이터베이스 연동: 
# FastAPI는 SQLAlchemy, Tortoise-ORM 등 다양한 ORM(Object-Relational Mapping) 라이브러리와 호환성을 제공하여 
# 데이터베이스 연동을 지원합니다. 
# FastAPI의 비동기 기능을 활용하면, 대규모 데이터베이스 작업을 효율적으로 처리할 수 있습니다. 
# FastAPI를 사용한 데이터베이스 연동은 고성능 웹 애플리케이션 개발에 매우 유용합니다.

# FastAPI는 Python 3.6+에서 작동하는 웹 프레임워크이다.
# FastAPI는 Starlette 프레임워크 위에서 작동하며, Starlette 프레임워크는 ASGI 서버와 호환된다.
# FastAPI는 Starlette 프레임워크의 기능을 확장하고, Pydantic을 사용하여 타입 힌트를 지원한다.
# FastAPI는 Swagger UI와 ReDoc를 자동으로 생성하여 API 문서화를 지원한다.

# pip install fastapi
# pip install "uvicorn[standard]"

# [Uvicorn을 사용하여 FastAPI 애플리케이션을 실행]
# uvicorn --help
# uvicorn FastAPI:app --reload 
# uvicorn FastAPI:app --host localhost --port 8001 --reload --workers 4
# uvicorn FastAPI:app --host 127.0.0.1 --port 8001 --reload --workers 4
# python -m uvicorn FastAPI:app --host 127.0.0.1 --port 8001 --reload --workers 4
# uvicorn.run(app, host='localhost', port=8001, log_level='info')

# FastAPI는 자동으로 OpenAPI 및 API 문서를 생성합니다. 서버가 실행 중일 때, 브라우저에서 다음 URL을 열어 문서를 확인할 수 있습니다:
# OpenAPI: http://127.0.0.1:8000/openapi.json
# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc: http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from pydantic import BaseModel # 데이터 유효성 검사
from typing import Optional

app = FastAPI()

# 사용자 데이터 모델 정의
class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

# 사용자 데이터 저장소
users = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 사용자 생성
@app.post("/users/{user_id}")
async def create_user(user_id: int, user: User):
    if user_id in users:
        return {"error": "User already exists"}
    users[user_id] = user
    return users[user_id]

# 사용자 조회
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users:
        return {"error": "User not found"}
    return users[user_id]

# 사용자 업데이트
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id not in users:
        return {"error": "User not found"}
    users[user_id] = user
    return users[user_id]

# 사용자 삭제
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users:
        return {"error": "User not found"}
    del users[user_id]
    return {"message": "User deleted"}

# async def app(scope, receive, send):
#     assert scope['type'] == 'http' # assert [조건], [오류메시지] => asset는 [조건]이 True인 경우 그대로 코드 진행, False인 경우 어설트에러 발생하게 됩니다.

#     await send({
#         'type': 'http.response.start',
#         'status': 200,
#         'headers': [
#             [b'content-type', b'text/plain'],
#         ],
#     })
#     await send({
#         'type': 'http.response.body',
#         'body': b'Hello, world!',
#     })

import uvicorn

#if __name__ == '__main__':
    #uvicorn.run(app, host='localhost', port=8001, log_level='info')
    
    # config = uvicorn.Config("FastAPI:app", port=8001, log_level="info")
    # server = uvicorn.Server(config)
    # server.run()
