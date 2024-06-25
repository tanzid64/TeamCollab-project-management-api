from django.urls import path, include
from rest_framework import routers
from projects.views import ProjectViewSet

router = routers.DefaultRouter()
router.register('', ProjectViewSet, basename="user-api")

urlpatterns = [
  path('', include(router.urls)),
]
