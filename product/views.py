from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Product ,Review
from .serializers import ProductSerializer,ProductListSerializer,ReviewSerializer
from .filters import ProductFilter
from django.core.paginator import Paginator
from django.db.models import Avg
@api_view(['GET'])
def product_list(request):
    
    products = Product.objects.all().order_by('-created_at')
    filterset = ProductFilter(request.GET , queryset=products)
    paginator = Paginator(filterset.qs, 2)  
        
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    serializer = ProductListSerializer(page_obj.object_list ,many = True, context={'request': request})
    return Response(serializer.data, status =status.HTTP_202_ACCEPTED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_detail(request,uuid):
    products = get_object_or_404(Product,uuid=uuid)
    serializer = ProductSerializer(products )
    return Response(serializer.data, status =status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def product_create(request):
   
    serializer = ProductSerializer( data = request.data)

    if serializer.is_valid():
        #print(request.user)
        serializer.save(user = request.user)
        #res = ProductSerializer(product,many=False)
 
        return Response({"product":serializer.data})
    else:
        return Response(serializer.errors)
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])    
def product_update(request,uuid):
    products = get_object_or_404(Product,uuid=uuid)
    serializer = ProductSerializer(products,data=request.data )
    if products.user!=request.user:
        return Response({'error':'this product is not your mine'})
    else:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors)
        
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])    
def product_delete(request,uuid):
    products = get_object_or_404(Product,uuid=uuid)
    if products.user!=request.user:
        return Response({'error':'this product is not your mine'})
    else:
        products.delete()
        return Response("prduct has been deleted",status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def review_create(request,uuid):
    user = request.user
    product = get_object_or_404(Product,uuid=uuid)
    data = request.data
    review = product.reviews.filter(user=user)
   
    if data['rating'] <= 0 or data['rating'] > 5:
        return Response({"error":'Please select between 1 to 5 only'}
                        ,status=status.HTTP_400_BAD_REQUEST) 
    elif review.exists():
        new_review = {'rating':data['rating'], 'body':data['body'] }
        review.update(**new_review)

        rating = product.reviews.aggregate(avg_ratings = Avg('rating'))
        product.ratings = rating['avg_ratings']
        product.save()

        return Response({'details':'Product review updated'})
    else:
        Review.objects.create(
            user=user,
            product=product,
            rating= data['rating'],
            body= data['body']
        )
        rating = product.reviews.aggregate(avg_ratings = Avg('rating'))
        product.ratings = rating['avg_ratings']
        product.save()
        return Response({'details':'Product review created'})
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_delete(request,uuid):
    user = request.user
    product = get_object_or_404(Product,uuid=uuid)
   
    review = product.reviews.filter(user=user)
   
 
    if review.exists():
        review.delete()
        rating = product.reviews.aggregate(avg_ratings = Avg('rating'))
        if rating['avg_ratings'] is None:
            rating['avg_ratings'] = 0
            product.ratings = rating['avg_ratings']
            product.save()
            return Response({'details':'Product review deleted'})
    else:
        return Response({'error':'Review not found'},status=status.HTTP_404_NOT_FOUND)