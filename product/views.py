from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    
    serializer = ProductSerializer(products,many = True)
    return Response(serializer.data, status =status.HTTP_202_ACCEPTED)

