from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()

    return Response({"Mustafa" : "Ahmed"})
