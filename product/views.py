from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer,ProductListSerializer
from .filters import ProductFilter
from django.core.paginator import Paginator

@api_view(['GET'])
def product_list(request):
    
    products = Product.objects.all().order_by('created_at')
    filterset = ProductFilter(request.GET , queryset=products)
    paginator = Paginator(filterset.qs, 2)  
        
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    serializer = ProductListSerializer(page_obj.object_list ,many = True, context={'request': request})
    return Response(serializer.data, status =status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def product_detail(request,uuid):
    products = get_object_or_404(Product,uuid=uuid)
    serializer = ProductSerializer(products )
    return Response(serializer.data, status =status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_create(request):
    data = request.data
    serializer = ProductSerializer(data = data)

    if serializer.is_valid():
        #print(request.user)
        product = Product.objects.create(**data,user=request.user)
        res = ProductSerializer(product,many=False)
 
        return Response({"product":res.data})
    else:
        return Response(serializer.errors)