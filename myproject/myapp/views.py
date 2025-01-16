from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer

# Create your views here.
# 뷰를 정의
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})
    #return HttpResponse("Hello, Django World!")

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        User.objects.create(name=name, email=email)
        return redirect('index')
    return render(request, 'add_user.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
