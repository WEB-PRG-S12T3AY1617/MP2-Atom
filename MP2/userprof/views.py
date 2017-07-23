from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import Post

def index(request):
    all_users = User.objects.all()
    context = {
        'all_u' : all_users,
        '/' : '/',
    }
    return render(request, 'homepage/userhpage.html', context)

def user(request, user_num):
    sUser = User.objects.get(id=user_num)
    context = {
        #'user_id' : user_num,
        'user' : sUser,
        'post' : Post.objects.get(id=sUser.id),
    }
    return render(request, 'usertemp/user.html', context)