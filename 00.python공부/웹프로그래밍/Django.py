##### Django #####
# Django는 고수준 웹 프레임워크로 강력한 기능과 다양한 내장 모듈을 제공합니다. 
# Django는 대규모 웹 애플리케이션 개발에 적합하며, 빠르고 안전한 개발을 위해 다양한 도구와 기능을 제공합니다.

# Django를 사용한 RESTful API 개발: 
# Django는 Django REST framework(DRF)라는 강력한 라이브러리를 통해 
# RESTful API 개발을 지원합니다. DRF는 직렬화, 인증, 권한 부여, 페이징, 필터링 등 
# RESTful API 개발에 필요한 모든 기능을 제공합니다. 
# 이를 통해 Django 애플리케이션과 완벽하게 통합된 RESTful API를 손쉽게 구축할 수 있습니다.

# Django는 MTV(Model-Template-View) 패턴을 기반으로 한다.
# Django는 ORM(Object-Relational Mapping)을 사용하여 데이터베이스와 상호작용한다.

# [주요 특징]
# - 빠른 개발: Django는 개발자가 최대한 빠르게 애플리케이션을 만들 수 있도록 도와줍니다. 
#   이를 위해 관리 인터페이스, ORM, URL 라우팅, 템플릿 엔진 등 다양한 기능을 기본으로 제공합니다.
# - 안전성: Django는 보안에 중점을 두고 설계되었습니다.
#   XSS(Cross Site Scripting), CSRF(Cross Site Request Forgery), SQL Injection 등 웹 애플리케이션의 일반적인 보안 문제를 예방하기 위한 다양한 기능을 내장하고 있습니다.
# - 확장성: Django는 모듈식 아키텍처를 사용하여 확장이 용이합니다. 애플리케이션의 요구사항에 맞게 쉽게 기능을 추가하거나 변경할 수 있습니다.
# - 재사용성: Django는 코드 재사용성을 높이기 위해 재사용 가능한 앱과 모듈을 지원합니다. 개발자는 이미 작성된 앱을 프로젝트에 쉽게 통합하여 사용할 수 있습니다.
# - 강력한 커뮤니티와 문서: Django는 강력한 커뮤니티와 풍부한 문서를 자랑합니다. 이를 통해 개발자는 문제를 해결하고, 새로운 기능을 배우는 데 큰 도움을 받을 수 있습니다.

# [주요 구성 요소]
# - ORM(Object-Relational Mapping): Django의 ORM은 데이터베이스 작업을 단순화하여, SQL을 직접 작성하지 않고도 데이터베이스와 상호작용할 수 있도록 도와줍니다. 이를 통해 데이터베이스 독립성을 유지하면서도 복잡한 데이터베이스 작업을 쉽게 처리할 수 있습니다.

# - 관리 인터페이스: Django는 자동으로 생성되는 관리 인터페이스를 제공합니다. 이를 통해 관리자나 개발자가 데이터베이스의 데이터를 쉽게 관리할 수 있습니다. 이 인터페이스는 매우 직관적이고 사용자 친화적입니다.
# - URL 라우팅: Django의 URL 라우팅 시스템은 클린하고 읽기 쉬운 URL을 정의할 수 있도록 도와줍니다. 이를 통해 웹 애플리케이션의 구조를 명확하게 유지하고, SEO(검색 엔진 최적화)를 개선할 수 있습니다.
# - 템플릿 엔진: Django의 템플릿 엔진은 HTML을 동적으로 생성할 수 있도록 도와줍니다. 템플릿 엔진은 상속, 조건문, 반복문 등을 지원하여 복잡한 웹 페이지를 쉽게 구성할 수 있습니다.
# - 폼 처리: Django는 폼 생성, 유효성 검사, 렌더링 등을 간편하게 처리할 수 있는 폼 프레임워크를 제공합니다. 이를 통해 사용자 입력을 쉽게 처리하고, 데이터의 유효성을 보장할 수 있습니다.]

# pip install django
# pip install djangorestframework <= Django REST Framework를 설치

# Django 프로젝트와 앱을 생성합니다.
# => django-admin startproject myproject
# => cd myproject
# => python manage.py startapp myapp

#### RESTful API ####
# 사용자 추가
# => curl -X POST -H "Content-Type: application/json" -d "{"name":"John","age":30}" http://localhost:8000/users/
# 사용자 조회
# => curl http://localhost:8000/users/1/
# 사용자 업데이트
# => curl -X PUT -H "Content-Type: application/json" -d "{"name":"John Doe","age":31}" http://localhost:8000/users/1/
# 사용자 삭제
# => curl -X DELETE http://localhost:8000/users/1/

import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

# Django settings
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='a_random_secret_key',
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

# View function
def index(request):
    return HttpResponse('Hello, Django!')

# URL patterns
urlpatterns = [
    path('', index),
]

# WSGI application
application = get_wsgi_application()

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
