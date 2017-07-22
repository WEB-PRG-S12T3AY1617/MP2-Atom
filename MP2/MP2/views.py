from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    #ada = '<h1>This is the Home page</h1>'
    #ada += '<nav><a href="homepage.html">Login</a><a href="homepage.html">Sign-up</a></nav></br>'
    #ada += '<a href="/users/">User Profiles</a>'
    #return HttpResponse(ada)
    #template = loader.get_template('userprof/templates/homepage/homepage.html')
    context = {
        
    }
    return render(request, 'homepage/Mainhpage.html', context)