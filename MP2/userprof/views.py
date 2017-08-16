from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .models import Post
from .models import profile
from .models import Offers
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .forms import RegisterForm, purchaseOfferForm, tradeOfferForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.template.defaultfilters import slugify

#updated
def index(request):

    all_post = Post.objects.all().order_by('-id') #updated

    context = allPaginate(request, all_post, 10)
    if request.user.is_authenticated():
        context['offers'] = Offers.objects.filter(post__op=request.user).order_by('-id')

    query = request.GET.get("q") #updated

    if query: #updated
        all_post = allQuery(request, query, all_post)
        posts = all_post
        context['posts'] = posts
        context['query'] = query
        context['offers'] = Offers.objects.filter(post__op=request.user).order_by('-id')
        return render(request, 'homepage/Mainhpage.html', context)

    return render(request, 'homepage/Mainhpage.html', context)#updated



#updated
def user(request, user_num):
    sUser = get_object_or_404(User,id=user_num)
    all_post = sUser.post_set.all().order_by('-id') #updated
    context = allPaginate(request, all_post, 5)
    context['user'] = sUser

    return render(request, 'homepage/user.html', context)




#updated
def login_user(request):
    posts = Post.objects.all().order_by('-id') #updated

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = allPaginate(request, posts, 10)
                return render(request, 'homepage/Mainhpage.html', context)
            else:
                return render(request, 'homepage/Mainhpage.html')
        else:
            context = allPaginate(request, posts, 10)
            context['error'] = 'Invalid Login'
            return render(request, 'homepage/Mainhpage.html', context)


def logout_user(request):
    logout(request)
    posts = Post.objects.all().order_by('-id')

    context = allPaginate(request, posts, 10)
    context['success'] = 'Account was successfully Logged out'
    return render(request, 'homepage/Mainhpage.html', context)

class createPost(CreateView):
    model = Post
    fields = ['item_name', 'thumbnail', 'quantity', 'post_condition', 'post_type', 'tags']

    def form_valid(self, form):
        form.instance.op = self.request.user
        return super(createPost,self).form_valid(form)

class createPurchaseOffer(CreateView):
    form_class = purchaseOfferForm
    template_name = 'userprof/offers_form.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk = self.kwargs['post_num'])
        form.instance.ifPurchase = True
        return super(createPurchaseOffer, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(createPurchaseOffer, self).get_context_data(**kwargs)
        context['log_user'] = self.request.user
        context['post_num'] = self.kwargs['post_num']
        return context
    def get_form_kwargs(self):
        kwargs = super(createPurchaseOffer, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class editPurchaseOffer(UpdateView):
    form_class = purchaseOfferForm
    template_name = 'userprof/offers_form.html'

    def get_object(self, queryset = None):
        obj = Offers.objects.get(id=self.kwargs['offers_id'])
        return obj
    def get_context_data(self, **kwargs):
        context = super(editPurchaseOffer, self).get_context_data(**kwargs)
        context['log_user'] = self.request.user
        context['offers'] = Offers.objects.filter(post__op=self.request.user).order_by('-id')
        return context
    def get_form_kwargs(self):
        kwargs = super(editPurchaseOffer, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class deleteOffer(DeleteView):
    model = Offers

    def get_object(self, queryset=None):
        obj = Offers.objects.get(id=self.kwargs['offers_id'])
        return obj

    def get_context_data(self, **kwargs):
        context = super(deleteOffer, self).get_context_data(**kwargs)
        context["log_user"] = self.request.user.id
        return context

    def get_success_url(self):
        return reverse( 'postdet', kwargs={'post_num': self.object.post_id})

class createTradeOffer(CreateView):
    form_class = tradeOfferForm
    template_name = 'userprof/offers_form.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk = self.kwargs['post_num'])
        form.instance.ifPurchase = False
        return super(createTradeOffer, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(createTradeOffer, self).get_context_data(**kwargs)
        context['log_user'] = self.request.user
        context['post_num'] = self.kwargs['post_num']
        return context
    def get_form_kwargs(self):
        kwargs = super(createTradeOffer, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class editTradeOffer(UpdateView):
    form_class = tradeOfferForm
    template_name = 'userprof/offers_form.html'

    def get_object(self, queryset = None):
        obj = Offers.objects.get(id=self.kwargs['offers_id'])
        return obj
    def get_context_data(self, **kwargs):
        context = super(editTradeOffer, self).get_context_data(**kwargs)
        context['log_user'] = self.request.user
        context['offers'] = Offers.objects.filter(post__op=self.request.user).order_by('-id')
        return context
    def get_form_kwargs(self):
        kwargs = super(editTradeOffer, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



#update
def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.degree = form.cleaned_data.get('degree')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.save()


            return render(request, 'homepage/Mainhpage.html', {'register' : 'Account was registered successfully'})
    else:
        form = RegisterForm()
    return render(request, 'homepage/register.html', {'form': form})



#updated
def post_detail(request, post_num):

    sPost = get_object_or_404(Post,id=post_num)
    if request.user.is_authenticated():
        
        return render(request, 'homepage/post_detail.html', {'post' : sPost, 'log_user': request.user , 'post_condition' : slugify(sPost.post_condition), 'offers': Offers.objects.filter(post__op=request.user).order_by('-id'), 'poffers': Offers.objects.filter(Q(post__id=post_num, post__op__id=request.user.id)).order_by('-id')})
    else:
        return render(request, 'homepage/post_detail.html', {'post' : sPost, 'log_user': request.user , 'post_condition' : slugify(sPost.post_condition)})




#updated
def indexPaginate(request, page_num):
    all_post = Post.objects.all().order_by('-id') #updated

    context = allPaginate(request, all_post, page_num)
    if request.user.is_authenticated():
        context['offers'] = Offers.objects.filter(post__op=request.user).order_by('-id')

    return render(request, 'homepage/Mainhpage.html', context)


def qPaginate(request, query, page_num):
    all_post = Post.objects.all().order_by('-id')
    all_post = allQuery(request, query, all_post)
    context = allPaginate(request, all_post, page_num)
    context['query'] = query
    return render(request, 'homepage/Mainhpage.html', context)


def allPaginate(request, obj, page_num):
    paginator = Paginator(obj, page_num)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts, 'page': page, 'log_user': request.user
    }
    if request.user.is_authenticated():
        context['offers'] = Offers.objects.filter(post__op=request.user).order_by('-id')
    return context


def allQuery(request, query, all_post):
    all_post = all_post.filter(
            Q(item_name__icontains=query) |
            Q(tags__slug__icontains=query) |
            Q(post_type__icontains=query) |
            Q(post_condition__icontains=query)
        ).distinct()
    return all_post

def TCTSearch(request, tag_name):
    all_post = Post.objects.all().order_by('-id')
    all_post = allQuery(request, tag_name, all_post)

    context = allPaginate(request, all_post, 10)
    context['query'] = tag_name
    return render(request, 'homepage/Mainhpage.html', context)
