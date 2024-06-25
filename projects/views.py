from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from projects.models import Project, ProjectMember
from projects.serializers import ProjectSerializer, ProjectMemberSerializer
# Create your views here.
class ProjectViewSet(ModelViewSet):
  serializer_class = ProjectSerializer
  queryset = Project.objects.all()
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class ProjectMemberViewSet(ModelViewSet):
  serializer_class = ProjectMemberSerializer
  http_method_names = ('get', 'delete', 'patch', 'post')
  def get_queryset(self):
    return ProjectMember.objects.filter(project_id=self.kwargs['project_id'])
  def perform_create(self, serializer):
    project_id = self.kwargs['project_id']
    serializer.save(project_id=project_id)