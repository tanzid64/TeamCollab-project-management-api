from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserRegisterView

router = routers.DefaultRouter()
# router.register('', UserViewSet, basename="user-api")

urlpatterns = [
  # path('users/', include(router.urls)),
  path("register/", UserRegisterView.as_view(), name="register-api"),
]