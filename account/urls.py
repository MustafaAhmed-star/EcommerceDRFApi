from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit/', views.user_update, name='user-update'),
    path('password/forgot/', views.password_forgot, name='password-forgot'),
    path('password/reset/toke', views.password_reset, name='password-reset'),
]