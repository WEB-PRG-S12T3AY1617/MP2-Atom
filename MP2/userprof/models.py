from django.db import models
from  django.core.validators import  MinValueValidator

class User(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    op = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    thumbnail = models.CharField(max_length=200)
    
    def __str__(self):
        return self.item_name
