from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from projects.models import Project
from projects.serializers import ProjectSerializer
# Create your views here.
class ProjectViewSet(ModelViewSet):
  serializer_class = ProjectSerializer
  queryset = Project.objects.all()
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)