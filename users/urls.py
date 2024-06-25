from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserRegisterView, UserLoginView, UserViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet, basename="user-api")

urlpatterns = [
  path('', include(router.urls)),
  path("register/", UserRegisterView.as_view(), name="register-api"),
  path("login/", UserLoginView.as_view(), name="login-api"),
]
