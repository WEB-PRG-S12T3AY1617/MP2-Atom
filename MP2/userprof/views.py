from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def index(request):
    all_users = User.objects.all()
    context = {
        'all_u' : all_users,
        '/' : '/',
    }
    return render(request, 'homepage/userhpage.html', context)

def user(request, user_num):
    context = {
        #'user_id' : user_num,
        'user' : User.objects.get(id=user_num)
    }
    return render(request, 'usertemp/user.html', context)