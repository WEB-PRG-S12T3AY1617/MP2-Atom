from django.conf.urls import url
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
    url(r'^login/$', views.login, name='login'),
    # /logout/
    url(r'^logout/$', views.logout, name='logout'),
]
