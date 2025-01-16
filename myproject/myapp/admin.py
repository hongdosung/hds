from django.contrib import admin

# Register your models here.
# 파일에서 관리자 인터페이스에 모델을 등록
from django.contrib import admin
from .models import User

admin.site.register(User)

# 관리자 계정을 생성하고, 관리자 인터페이스를 실행합니다
# python manage.py createsuperuser
# python manage.py runserver
