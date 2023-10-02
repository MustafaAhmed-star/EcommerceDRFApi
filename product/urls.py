from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/create/', views.product_create, name='product-create'),
    path('products/<uuid:uuid>/', views.product_detail, name='product-detail'),
    path('products/<uuid:uuid>/edit/', views.product_update, name='product-update'),
]
