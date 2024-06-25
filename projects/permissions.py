from rest_framework import permissions
from .models import Project, ProjectMember

class IsProjectOwnerOrAdminMember(permissions.BasePermission):
  """
  - Anyone can view projects
  - Only project owners & admin members can edit projects
  - Only project owners can delete projects
  - Superusers can have all access
  """

  def has_object_permission(self, request, view, obj):
    # Allow superusers to have all access
    if request.user.is_superuser:
      return True
    # Allow any one can get access
    if request.method == 'GET':
      return True
    # Allow project owners and admin members to edit projects
    if request.method in ['PUT', 'PATCH']:
      if obj.owner == request.user:
        return True
      try:
        isAdminMember = ProjectMember.objects.filter(project=obj, user=request.user, role='Admin').exists()
      except ProjectMember.DoesNotExist:
        isAdminMember = False
      if isAdminMember:
        return True
    # Allow project owners to delete projects
    if request.method == 'DELETE':
      if obj.owner == request.user:
        return True
    return False

class IsProjectMemberAdminOrOwner(permissions.BasePermission):
  """
  - Project Owner & members can view all members
  - Admin members & project owners can add, edit or delete members
  - Superusers can have all access
  """

  def has_permission(self, request, view):
    # # Check if the user is a superuser (Django admin)
    if request.user.is_superuser:
      return True
    # Get the project
    try:
      project_id = view.kwargs.get('project_id')
      project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
      return False
    if project:
      # Allow member to view all members
      if request.method == 'GET':
        return ProjectMember.objects.filter(project=project_id, user=request.user).exists() or project.owner == request.user
      # Allow admin members or project owner to add, edit or delete members
      if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
        return ProjectMember.objects.filter(project=project_id, user=request.user, role='Admin').exists() or project.owner == request.user

    return False
