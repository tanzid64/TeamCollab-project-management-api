from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from users.models import User
from users.serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Simple JWT
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
  }

class UserRegisterView(generics.CreateAPIView):
  serializer_class = UserRegisterSerializer

class UserLoginView(generics.GenericAPIView):
  serializer_class = UserLoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    return Response(get_tokens_for_user(user), status=status.HTTP_200_OK)

