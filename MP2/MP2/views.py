from django.shortcuts import render
from userprof.models import Post

def index(request):

    all_post = Post.objects.all()

    return render(request, 'homepage/Mainhpage.html', {'all_p' : all_post})