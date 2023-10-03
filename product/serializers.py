from rest_framework import serializers
from .models import Product,Review

class ProductSerializer(serializers.ModelSerializer):
 
   class Meta:
        model = Product
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):

   url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='uuid')

   class Meta:
      model = Product
      #fields = '__all__'
      exclude = ['created_at','uuid']

class ReviewSerializer(serializers.ModelSerializer):
 
   class Meta:
        model = Review
        fields = '__all__'