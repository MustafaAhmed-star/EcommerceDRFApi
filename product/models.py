import uuid
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
    # Using unique id to more secure
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=30,choices=Category.choices)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
class Review(models.Model):

    body = models.TextField(max_length=250,default=" ")
    rating = models.DecimalField(max_digits=2,decimal_places=1,default=0)
    product = models.ForeignKey(Product,null=True,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at','rating']

    def __str__(self):
        return f' {self.user}-->{self.rating}'