from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from users.models import User
from users.serializers import UserRegisterSerializer, UserLoginSerializer, UserDetailsSerializer
from users.permissions import IsAdminOrIsSelf
from rest_framework_simplejwt.tokens import RefreshToken

# Simple JWT
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
  }

# User Registration
class UserRegisterView(generics.CreateAPIView):
  serializer_class = UserRegisterSerializer

# User Login
class UserLoginView(generics.GenericAPIView):
  serializer_class = UserLoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    tokens = get_tokens_for_user(user)
    return Response(tokens, status=status.HTTP_200_OK)
  
# User Details, Update, Delete
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserDetailsSerializer
  permission_classes = [IsAdminOrIsSelf]
  http_method_names = ('get', 'delete', 'patch')

