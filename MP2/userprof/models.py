from django.db import models
from  django.core.validators import  MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from taggit.managers import TaggableManager

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default = False)
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
    POST_TYPE_CHOICES=(
        ('Academic', 'Academic'),
        ('Non-Academic', 'Non-Academic'),
    )
    post_type = models.CharField(max_length = 20, choices = POST_TYPE_CHOICES, default = 'Academic')
    POST_CONDITION_CHOICES = (
        ('USED', 'Used'),
        ('BNEW', 'Brand New'),
    )
    post_condition = models.CharField(max_length = 4, choices = POST_CONDITION_CHOICES, default = 'BNEW')
    academic_subject = models.CharField(max_length = 7, blank = True)
    tags = TaggableManager()

    def __str__(self):
        return self.item_name
