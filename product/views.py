from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer,ProductListSerializer
from .filters import ProductFilter
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    filterset = ProductFilter(request.GET , queryset=products)
    serializer = ProductListSerializer(filterset.qs,many = True, context={'request': request})
    return Response(serializer.data, status =status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def product_detail(request,uuid):
    products = get_object_or_404(Product,uuid=uuid)
    serializer = ProductSerializer(products,context={'request': request})
    return Response(serializer.data, status =status.HTTP_202_ACCEPTED)

