from django.db import models

# Create your models here.
# 데이터 모델을 정의
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    #age = models.IntegerField()

    def __str__(self):
        return self.name

# 모델을 데이터베이스에 반영하기 위해 마이그레이션을 생성하고 적용
# python manage.py makemigrations
# python manage.py migrate
