from django.shortcuts import render, get_object_or_404
from .models import User
from .models import Post
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

def index(request):

    all_post = Post.objects.all()

    return render(request, 'homepage/Mainhpage.html', {'all_p' : all_post})

def all_user(request):
    all_users = User.objects.all()
    return render(request, 'homepage/userhpage.html', {'all_u' : all_users,
        '/' : '/', 'currdirect' : 2})

def user(request, user_num):
    sUser = get_object_or_404(User,id=user_num)
<<<<<<< HEAD
    return render(request, 'usertemp/user.html', {'user' : sUser,
        'all_upost' : sUser.post_set.all()})


class UserFormView(View):
    form_class = User
    template_name = 'userprof/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
=======
    return render(request, 'homepage/user.html', {'user' : sUser,
        'all_upost' : sUser.post_set.all(), 'currdirect' : 3})

def register(request):
    return render(request, 'homepage/reghpage.html', {})

def login(request):
    return render(request, 'homepage/loghpage.html', {})
>>>>>>> 21bc0953cbfee99aaee12e47af225949f342d055
