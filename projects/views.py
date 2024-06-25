from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from projects.models import Project, ProjectMember
from projects.serializers import ProjectSerializer, ProjectMemberSerializer
from projects.permissions import IsProjectOwnerOrAdminMember, IsProjectMemberAdminOrOwner
# Create your views here.
class ProjectViewSet(ModelViewSet):
  serializer_class = ProjectSerializer
  permission_classes = (IsAuthenticatedOrReadOnly, IsProjectOwnerOrAdminMember)
  queryset = Project.objects.all()
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class ProjectMemberViewSet(ModelViewSet):
  serializer_class = ProjectMemberSerializer
  permission_classes = (IsAuthenticatedOrReadOnly, IsProjectMemberAdminOrOwner)
  http_method_names = ('get', 'delete', 'patch', 'post')
  def get_queryset(self):
    return ProjectMember.objects.filter(project_id=self.kwargs['project_id'])
  def perform_create(self, serializer):
    project_id = self.kwargs['project_id']
    serializer.save(project_id=project_id)