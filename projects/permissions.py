from rest_framework import permissions
from .models import Project, ProjectMember

class IsProjectOwnerOrAdminMember(permissions.BasePermission):
  """
  Custom permission to only allow owners of a project or admin members to edit it.
  """

  def has_object_permission(self, request, view, obj):
    # Check if the user is a superuser (Django admin)
    if request.user.is_superuser:
      return True

    # Check if the object is a Project instance
    if isinstance(obj, Project):
      # Project owner can update or delete
      if obj.owner == request.user:
        return True

      # Project members with role 'Admin' can update
      project_member = ProjectMember.objects.filter(project=obj, user=request.user, role='Admin').exists()
      if project_member:
        return True

    return False

class IsProjectMemberAdminOrOwner(permissions.BasePermission):
  """
  Custom permission to only allow project owners or admin members to edit project members.
  """

  def has_object_permission(self, request, view, obj):
    # Check if the user is a superuser (Django admin)
    if request.user.is_superuser:
      return True

      # Check if the object is a ProjectMember instance
    if isinstance(obj, ProjectMember):
        # Project owner can update or delete ProjectMember
        if obj.project.owner == request.user:
            return True

        # Project members with role 'Admin' can update ProjectMember
        project_member = ProjectMember.objects.filter(project=obj.project, user=request.user, role='Admin').exists()
        if project_member:
            return True

    return False
