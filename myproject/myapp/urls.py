from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

# URL 패턴을 설정
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.user_list, name='user_list'),
    path('add/', views.add_user, name='add_user'),
    path('', include(router.urls)),
]
