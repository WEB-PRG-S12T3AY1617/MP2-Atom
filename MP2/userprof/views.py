from django.shortcuts import render, get_object_or_404
from .models import User
from .models import Post

def index(request):

    all_post = Post.objects.all()

    return render(request, 'homepage/Mainhpage.html', {'all_p' : all_post})

def all_user(request):
    all_users = User.objects.all()
    return render(request, 'homepage/userhpage.html', {'all_u' : all_users,
        '/' : '/', 'currdirect' : 2})

def user(request, user_num):
    sUser = get_object_or_404(User,id=user_num)
    return render(request, 'homepage/user.html', {'user' : sUser,
        'all_upost' : sUser.post_set.all(), 'currdirect' : 3})

def register(request):
    return render(request, 'homepage/reghpage.html', {})

def login(request):
    return render(request, 'homepage/loghpage.html', {})