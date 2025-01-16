#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# python manage.py startapp myapp

# python manage.py startapps
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver
# => http://localhost:8000/users/ 

# $python manage.py	develop runserver
# => develop 환경으로 runserver
# $python manage.py	product migrate
# => product 환경으로 migrate
# $python manage.py shell
# => develop 환경으로 shell 접속

### 관리자 페이지나 Django 쉘을 사용하여 일부 사용자 데이터를 추가
# python manage.py shell
# >>> from myapp.models import User
# >>> User.objects.create(name='Alice', email='alice@example.com')
# >>> User.objects.create(name='Bob', email='bob@example.com')

def main():
    """Run administrative tasks."""
    # 환경변수에 'DJANGO_SETTINGS_MODULE'라는 이름으로 config.local.settings라는 문자열을 등록시켜주는 명령어
    # os.environ : 현재 시스템의 환경 변수에 대한 정보를 가지고 있는 딕셔너리
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    
    # if 'production' in sys.argv:
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.production')
    #     sys.argv.remove('production')
    # elif 'develop' in sys.argv:
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.develop')
    #     sys.argv.remove('develop')
    # else:
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.local')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
