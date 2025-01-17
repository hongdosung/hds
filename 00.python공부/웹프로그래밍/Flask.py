##### Flask #####
# Flask는 Python으로 작성된 경량 웹 프레임워크로, 단순하고 유연한 설계를 자랑합니다. 
# Flask는 최소한의 기능만을 포함하고 있으며, 필요한 기능은 확장 패키지를 통해 추가할 수 있습니다. 
# 이를 통해 개발자는 프로젝트의 요구 사항에 맞게 프레임워크를 유연하게 구성할 수 있습니다.

# Flask를 사용한 RESTful API 개발: 
# Flask는 URL 라우팅, 요청 처리, 응답 생성 등 
# RESTful API 개발에 필요한 기본 기능을 쉽게 구현할 수 있도록 지원합니다. 
# Flask의 확장 패키지를 사용하면, 인증, 데이터 검증, 문서화 등의 기능을 추가하여 완전한 RESTful API를 구축할 수 있습니다.

# [주요 특징]
# - 경량 프레임워크: Flask는 최소한의 기능만을 포함하고 있으며, 필요한 기능은 확장 패키지를 통해 추가할 수 있습니다. 이를 통해 개발자는 프로젝트의 요구 사항에 맞게 프레임워크를 유연하게 구성할 수 있습니다.
# - 유연한 URL 라우팅: Flask는 URL 라우팅을 쉽게 설정할 수 있도록 지원합니다. 이는 다양한 URL 경로에 대해 특정 함수를 실행할 수 있게 하여, 웹 애플리케이션의 라우팅 구조를 간단하게 정의할 수 있습니다.
# - 템플릿 엔진: Flask는 Jinja2라는 강력한 템플릿 엔진을 사용합니다. Jinja2는 HTML을 동적으로 생성하고, 템플릿 상속, 조건문, 반복문 등의 기능을 지원하여 복잡한 웹 페이지를 쉽게 구성할 수 있습니다.
# - 확장 가능성: Flask는 확장 가능한 구조를 가지고 있습니다. 이를 통해 ORM, 폼 처리, 인증, 파일 업로드 등 다양한 기능을 플러그인 형태로 추가할 수 있습니다. Flask의 확장 패키지는 Flask 플러그인 생태계를 통해 제공되며, 이를 사용하여 애플리케이션을 빠르게 확장할 수 있습니다.
# - 테스트 지원: Flask는 단위 테스트 및 통합 테스트를 쉽게 작성할 수 있도록 도와줍니다. Flask의 테스트 클라이언트를 사용하면, 실제 서버를 실행하지 않고도 애플리케이션의 동작을 테스트할 수 있습니다.

# [주요 구성 요소]
# - Flask 클래스: Flask 애플리케이션의 중심이 되는 클래스입니다. 이 클래스는 애플리케이션의 설정, 라우팅, 요청 처리 등의 기능을 관리합니다.
# - 라우팅: @app.route 데코레이터를 사용하여 URL과 함수를 매핑합니다. 이를 통해 특정 URL로 요청이 들어왔을 때 실행될 함수를 정의할 수 있습니다.
# - 요청 객체: 클라이언트로부터의 HTTP 요청 정보를 담고 있는 객체입니다. 이를 사용하여 요청 메서드(GET, POST 등), 폼 데이터, 파일 업로드, 쿠키 등의 정보를 처리할 수 있습니다.
# - 응답 객체: 서버에서 클라이언트로 전송할 HTTP 응답 정보를 담고 있는 객체입니다. 이를 사용하여 응답 상태 코드, 헤더, 본문 등을 설정할 수 있습니다.
# - 템플릿 엔진: Jinja2 템플릿 엔진을 사용하여 HTML을 동적으로 생성합니다. 템플릿 파일은 애플리케이션의 템플릿 디렉토리에 저장되며, render_template 함수를 사용하여 렌더링됩니다.

# RESTful API는 HTTP 메서드(예: GET, POST, PUT, DELETE)를 사용하여 리소스를 생성, 읽기, 업데이트, 삭제하는 작업을 수행합니다.

# pip install Flask
# pip install Flask-RESTful

from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__) # Flask 클래스를 사용하여 애플리케이션 인스턴스를 생성하고, 라우트를 설정하여 요청을 처리
api = Api(app)

# 라우팅 설정
@app.route('/') # 데코레이터를 사용하여 URL과 처리 함수를 연결
def index():
    return "Hello, World!"

@app.route('/hello/<name>')
def hello(name):
    #return f"Hello, {name}!"
    # render_template 함수를 사용하여 index.html 템플릿을 렌더링하고, name 변수를 템플릿에 전달합니다.
    return render_template('index.html', name=name)

@app.route('/form', methods=['GET', 'POST', 'PUT', 'DELETE'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            <input type="submit" value="Submit">
        </form>
    '''

users = {} # 사용자 정보를 저장할 딕셔너리

# 사용자 정보를 처리하는 API 리소스를 정의합니다.
class User(Resource):
    def get(self, user_id):
        if user_id not in users:
            return {"message": "User not found"}, 404
        if user_id == "all":
            return users
        return users[user_id]

    def post(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        #parser.add_argument("likes", type=str, required=True, help="name on the video")
        args = parser.parse_args()

        if user_id in users:
            return {"message": "User already exists"}, 400

        users[user_id] = {"name": args["name"], "age": args["age"]}
        return users[user_id], 201

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        args = parser.parse_args()

        if user_id not in users:
            return {"message": "User not found"}, 404

        users[user_id] = {"name": args["name"], "age": args["age"]}
        return users[user_id]

    def delete(self, user_id):
        if user_id not in users:
            return {"message": "User not found"}, 404
        del users[user_id]
        return {"message": "User deleted"}

# API 경로를 설정하여 리소스를 연결합니다.
api.add_resource(User, "/user/<string:user_id>")

if __name__ == '__main__':
    app.run(debug=True)

# 코드로 간단한 사용자 관리 RESTful API가 완성되었습니다. Postman 또는 cURL을 사용하여 API를 테스트할 수 있습니다.
# 사용자 추가
# curl -X POST http://localhost:5000/user/2 -H "Content-type:application/json" -d "name=John11&age=55"

# 사용자 조회
# curl http://localhost:5000/user/1

# 사용자 업데이트
# curl -X PUT -d "name=John Doe&age=31" http://localhost:5000/user/2 -H "Content-type:application/json"

# 사용자 삭제
# curl -X DELETE http://localhost:5000/user/1

# curl -X GET http://localhost:5000/status | jq
