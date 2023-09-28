from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<uuid:uuid>/', views.product_detail, name='product-detail'),
]
