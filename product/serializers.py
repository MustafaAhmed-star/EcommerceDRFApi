from rest_framework import serializers
from .models import Product,Review

class ProductSerializer(serializers.ModelSerializer):
 
   class Meta:
        model = Product
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):

   url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='uuid')
   reviews = serializers.SerializerMethodField(method_name='get_reviews',read_only = True)

   class Meta:
      model = Product
      #fields = '__all__'
      exclude = ['created_at','uuid']
   def get_reviews(self,obj):
      reviews = obj.reviews.all()
      serializers = ReviewSerializer(reviews,many = True)
      return serializers.data
class ReviewSerializer(serializers.ModelSerializer):
   
   class Meta:
        model = Review
        fields = '__all__'