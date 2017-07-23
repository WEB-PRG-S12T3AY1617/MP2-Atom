from django.shortcuts import render
from userprof.models import Post

app_name = 'main'

def index(request):

    all_post = Post.objects.all()

    return render(request, 'homepage/Mainhpage.html', {'all_p' : all_post})