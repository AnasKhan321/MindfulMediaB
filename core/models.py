from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# Create your models here.
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Book = models.TextField(null=True)
#     Price = models.CharField(default="", max_length=90)
#     Update = models.CharField(default="", max_length=150)
#     date = models.DateTimeField(default=datetime.now(), blank=True)
#     def __str__(self):
#         return self.user.username

class Books(models.Model):
    Name = models.CharField(default="",max_length=90)
    Category = models.CharField(default="",max_length=40)
    image = models.ImageField(upload_to='bookimg')
    Summary = models.TextField(null=True)
    url_img = models.CharField(default="",max_length=900)
    Price = models.CharField(default="",max_length=200)

    def __str__(self):
        return  self.Name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(default="",max_length=200)
    Price = models.CharField(default="",max_length=90)
    Update = models.CharField(null=True,max_length=200)
    Address1 = models.CharField(default="",max_length=300)
    Address2 = models.CharField(default="",max_length=200)
    State = models.CharField(default="",max_length=90)
    City = models.CharField(default="",max_length=90)

    def __str__(self):
        return  self.user.username


class Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Address1 = models.CharField(default="",max_length=300)
    Address2 = models.CharField(default="",max_length=200)
    State = models.CharField(default="",max_length=70)
    City = models.CharField(default="",max_length=100)

    def __str__(self):
        return  self.user.username
