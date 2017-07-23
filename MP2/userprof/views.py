from django.shortcuts import render, get_object_or_404
from .models import User
from .models import Post

app_name = 'userprof'

def index(request):
    all_users = User.objects.all()
    return render(request, 'homepage/userhpage.html', {'all_u' : all_users,
        '/' : '/',})

def user(request, user_num):
    sUser = get_object_or_404(User,id=user_num)
    return render(request, 'usertemp/user.html', {'user' : sUser,
        'all_upost' : sUser.post_set.all()})