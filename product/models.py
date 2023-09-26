from django.db import models
from django.contrib.auth.models import User


class Category(models.TextChoices):
    Electronics ='electronics'
    Clothing ='Clothing'
    Shoes = 'Shoes'
    Home ='Home'
    Kitchen='Kitchen'
    Beauty  ='Beauty'
    Books ='Books'
    Pet = 'Pet'
    Sports = 'Sports'
    Toys = 'Toys'
    Health = 'Health'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=30,choices=Category.choices)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)