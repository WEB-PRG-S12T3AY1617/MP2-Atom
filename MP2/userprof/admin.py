from django.contrib import admin
from .models import profile
from django.contrib.auth.models import User
from .models import Post, Offers

admin.site.register(profile)
admin.site.register(Post)
admin.site.register(Offers)
