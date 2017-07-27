from django.db import models
from  django.core.validators import  MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, blank = True)

@receiver(post_save, sender = User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user = instance)
    instance.profile.save()



class Post(models.Model):
    op = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    thumbnail = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name
