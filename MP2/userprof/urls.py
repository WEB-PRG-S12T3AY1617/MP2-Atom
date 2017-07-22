from django.conf.urls import url
from . import views

urlpatterns = [
    #/users/
    url(r'^$', views.index, name='index'),
    #/users/[userid]/
    url(r'^(?P<user_num>[0-9]+)/$', views.user, name='user'),
]