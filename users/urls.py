from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserRegisterView, UserLoginView, UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register('', UserViewSet, basename="user-api")

urlpatterns = [
  path("register/", UserRegisterView.as_view(), name="register-api"),
  path("login/", UserLoginView.as_view(), name="login-api"),
  path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh-api"),
  path('', include(router.urls)),
]
