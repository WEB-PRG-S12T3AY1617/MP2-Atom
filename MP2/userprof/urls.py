from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    #//
    url(r'^$', views.index, name='index'),
    #/users/
    url(r'^users/$', views.all_user, name='all_user'),
    #/users/[userid]/
    url(r'^users/(?P<user_num>[0-9]+)/$', views.user, name='user'),
    #/register/
    url(r'^register/$', views.Register, name='register'),
    #/login/
    url(r'^login/', auth_views.login,{'template_name': 'homepage/loghpage.html'} ,name='login', ),
    # /logout/
    url(r'^logout/', auth_views.logout,{'template_name': 'homepage/logoutpage.html'}, name='logout', ),
]
