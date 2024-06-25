from django.shortcuts import render
from rest_framework import generics, viewsets
from users.models import User
from users.serializers import UserRegisterSerializer
# Create your views here.
class UserRegisterView(generics.CreateAPIView):
  serializer_class = UserRegisterSerializer

