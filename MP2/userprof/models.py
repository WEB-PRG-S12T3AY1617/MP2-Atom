from django.db import models
from  django.core.validators import  MinValueValidator

class User(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)

class Post(models.Model):
    op = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    thumbnail = models.CharField(max_length=200)
    
