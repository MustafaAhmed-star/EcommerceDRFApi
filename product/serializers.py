from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model= Product
        #exclude=["created_at"]
        fields = [ 'name', 'description', 'price', 'brand','category','rating','stock','user']