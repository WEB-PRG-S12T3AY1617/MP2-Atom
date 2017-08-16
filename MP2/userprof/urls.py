from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    #//
    url(r'^$', views.index, name='index'),

    #/paginate_by=[numpage]/
    url(r'^paginate_by=(?P<page_num>[0-9]+)/$', views.indexPaginate, name='indexPage'), #updated

    #/search_results/?q=
    url(r'^search_results/$', views.index, name='search'),

    #/search_results/[query]/paginate_by=[numpage]/
    url(r'^search_results/(?P<query>[-\w]+)/paginate_by=(?P<page_num>[0-9]+)/$', views.qPaginate, name='qPage'), #updated

    #/search_by_tag/[tag_name]
    url(r'^search_by_tag/(?P<tag_name>[-\w]+)/$', views.TCTSearch, name='searchTg'),

    #/search_by_condtion/[condtion]
    url(r'^search_by_condtion/(?P<tag_name>[-\w]+)$', views.TCTSearch, name='searchC'),

    #/search_by_type/[type]
    url(r'^search_by_type/(?P<tag_name>[-\w]+)$', views.TCTSearch, name='searchTy'),

    #/users/[userid]/
    url(r'^users/(?P<user_num>[0-9]+)/$', views.user, name='user'),

    #/post/[postid]/
    url(r'^post/(?P<post_num>[0-9]+)/$', views.post_detail, name='postdet'), #updated

    #/register/
    url(r'^register/$', views.Register, name='register'),

    #/login/
    url(r'^login/', views.login_user,name='login'), #updated

    # /logout/
    url(r'^logout/', views.logout_user, name='logout', ), #updated

    url(r'^createpost/', views.createPost.as_view(success_url = "/"), name='createpost', ),

    #/post/[postid]/addoffer/purchase
    url(r'^post/(?P<post_num>[0-9]+)/addoffer/purchase/$',views.createPurchaseOffer.as_view(success_url = "/"), name='purchase'),
    #/post/[postid]/addoffer/trade
    url(r'^post/(?P<post_num>[0-9]+)/addoffer/trade/$', views.createTradeOffer.as_view(success_url = "/"), name='trade'),

    #/post/[postid]/editoffer/purchase/[offers-id]
    url(r'^post/(?P<post_num>[0-9]+)/editoffer/purchase/(?P<offers_id>[0-9]+)$',views.editPurchaseOffer.as_view(success_url = "/"), name='editpurchase'),
    #/post/[postid]/editoffer/purchase/[offers-id]
    url(r'^post/(?P<post_num>[0-9]+)/editoffer/trade/(?P<offers_id>[0-9]+)$',views.editTradeOffer.as_view(success_url = "/"), name='edittrade'),

    url(r'^post/(?P<post_num>[0-9]+)/deleteoffer/(?P<offers_id>[0-9]+)$',views.deleteOffer.as_view(success_url = "/"), name='deleteoffer'),
]
