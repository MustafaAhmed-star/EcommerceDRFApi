from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/create/', views.product_create, name='product-create'),
    path('products/<uuid:uuid>/', views.product_detail, name='product-detail'),
    path('products/<uuid:uuid>/edit/', views.product_update, name='product-update'),
    path('products/<uuid:uuid>/delete/', views.product_delete, name='product-delete'),
    path('<uuid:uuid>/review/', views.review_create, name='review-create'),
    path('<uuid:uuid>/review/delete/', views.review_delete, name='review-delete'),

]
