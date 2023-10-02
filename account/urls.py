from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit/', views.user_update, name='user-update'),
]