from django.shortcuts import render
from django.template import loader

app_name = 'register'

def index(request):
    return render(request, 'homepage/reghpage.html', {})
