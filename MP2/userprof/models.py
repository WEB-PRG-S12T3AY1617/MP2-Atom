from django.db import models
from  django.core.validators import  MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default = True)
    degree = models.CharField(max_length=50, blank = True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender = User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user = instance)
    instance.profile.save()



class Post(models.Model):
    op = models.ForeignKey(User, on_delete=models.CASCADE,)
    item_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    thumbnail = models.FileField()
    POST_TYPE_CHOICES=(
        ('Academic', 'Academic'),
        ('Non-Academic', 'Non-Academic'),
    )
    post_type = models.CharField(max_length = 20, choices = POST_TYPE_CHOICES, default = 'Academic')
    POST_CONDITION_CHOICES = (
        ('Used', 'Used'),
        ('Brand New', 'Brand New'),
    )
    post_condition = models.CharField(max_length = 20, choices = POST_CONDITION_CHOICES, default = 'BNEW')
    academic_subject = models.CharField(max_length = 7, blank = True)
    tags = TaggableManager()

    def __str__(self):
        return self.item_name


class Offers(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ifPurchase = models.BooleanField(default = True)
    amount = models.PositiveIntegerField(default = 0)
    item = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'offered_item', null=True, blank=True)
    confirmed = models.BooleanField(default = False)
    reason = models.CharField(max_length = 500, blank=True)
