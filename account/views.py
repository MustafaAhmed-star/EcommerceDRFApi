from django.shortcuts import get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SignUpSerializer,UserSerializer
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from django.core.mail import send_mail


@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username = data['email']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                username = data['email'],
                password =make_password(data['password']),
            )
            return Response('Your account is registered sucesfully',status=status.HTTP_201_CREATED)
        else:
            return Response('This  account is already registered Try another one',status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors)


@api_view(['PUT'])
def user_update(request):
    user = request.user
    serializer= UserSerializer(user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def password_forgot(request):
    data = request.data
    email = data.get('email')

    if not email:
        return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, email=email)

    token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes=30)

    profile = user.profile
    profile.reset_password_token = token
    profile.reset_password_expire = expire_date
    profile.save()

    reset_link = f"http://localhost:8000/api/password/reset/{token}"
    body = f"Your password reset link is: {reset_link}"

    send_mail(
        subject="Password reset from eMarket",
        message=body,
        from_email="eMarket@gmail.com",
        recipient_list=[email]
    )

    return Response({'details': f'Password reset sent to {email}'})
@api_view(['POST'])
def password_reset(request,token):
    data = request.data
    user = get_object_or_404(User,profile__reset_password_token = token)

    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return Response({'error': 'Token is expired'},status=status.HTTP_400_BAD_REQUEST)
    
    if data['password'] != data['confirmPassword']:
        return Response({'error': 'Password are not same'},status=status.HTTP_400_BAD_REQUEST)
    
    user.password = make_password(data['password'])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None 
    user.profile.save() 
    user.save()
    return Response({'details': 'Password reset done '})

    