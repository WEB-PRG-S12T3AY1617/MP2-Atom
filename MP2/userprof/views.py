from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .models import Post
from .models import profile
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import View
from django.contrib.auth import views as auth_views
from .forms import RegisterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def index(request):

    all_post = Post.objects.all()
    paginator = Paginator(all_post, 2)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)


        #    filterLimit = Q()
        #
        #    if 'q' in request.GET:
        #        tags = request.GET['q'].split()
        #        for tag in tags:
        #            filterLimit = filterLimit | Q(tags__contains=tag)
        # 'all_p' : all_post,
        #    all_post = all_post.filter(filterLimit)

    return render(request, 'homepage/Mainhpage.html', {'posts': posts, 'page': page})

def all_user(request):
    all_users = User.objects.all()
    return render(request, 'homepage/userhpage.html', {'all_u' : all_users,
        '/' : '/', 'currdirect' : 2})

def user(request, user_num):
    sUser = get_object_or_404(User,id=user_num)
    posts = sUser.post_set.all()

    filterLimit = Q()
    if 'q' in request.GET:
        tags = request.GET['q'].split()
        for tag in tags:
            filterLimit = filterLimit | Q(tags__contains=tag)

    posts = posts.filter(filterLimit)
    return render(request, 'homepage/user.html', {'user' : sUser,
        'all_upost' : posts, 'currdirect' : 3})

def register(request):
    return render(request, 'homepage/reghpage.html', {})

def login(request):

    return render(request, 'homepage/loghpage.html', {})

def logout(request):
    return render(request, 'homepage/logoutpage.html', {})


def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.degree = form.cleaned_data.get('degree')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request)
            messages.success(request, 'Your profile has been added.')
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'homepage/register.html', {'form': form})
