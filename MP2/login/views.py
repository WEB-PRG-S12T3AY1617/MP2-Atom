from django.shortcuts import render
from django.template import loader

app_name = 'login'

def index(request):
    return render(request, 'homepage/loghpage.html', {})
