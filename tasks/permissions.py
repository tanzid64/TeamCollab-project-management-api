from rest_framework import permissions
from projects.models import Project, ProjectMember
from tasks.models import Task, Comments

class IsTaskCreateAllowed(permissions.BasePermission):
  """
  - Project Owner & admin members can create tasks.
  - Project members with role 'Member' can only view tasks.
  - Superusers can have all access.
  """

  def has_permission(self, request, view):
    # Allow superusers to have all access
    if request.user.is_superuser:
      return True

    project_id = view.kwargs.get('project_id')
    if not project_id:
      return False

    try:
      project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
      return False

    # Allow project owners to create tasks
    if project.owner == request.user:
      return True

    # Allow project members with role 'Admin' to create tasks
    if ProjectMember.objects.filter(project=project, user=request.user.id, role='Admin').exists():
      return True

    # Allow project members with role 'Member' to only view tasks
    if request.method in permissions.SAFE_METHODS:
      if ProjectMember.objects.filter(project=project, user=request.user.id, role='Member').exists():
        return True or project.owner == request.user

    return False

class IsTaskUpdateAllowed(permissions.BasePermission):
  """
  - Project Owner & admin members can update tasks.
  - Project members with role 'Member' can only view tasks.
  - Superusers can have all access.
  """

  def has_object_permission(self, request, view, obj):
    # Allow superusers to have all access
    if request.user.is_superuser:
      return True

    try:
      project = obj.project
    except Project.DoesNotExist:
      return False

    # Allow project owners to update tasks
    if project.owner == request.user:
      print(project.owner)
      return True

    # Allow project members with role 'Admin' to update tasks
    if ProjectMember.objects.filter(project=project, user=request.user.id, role='Admin').exists():
      return True

    # Allow project members with role 'Member' to only view tasks
    if request.method in permissions.SAFE_METHODS:
      if ProjectMember.objects.filter(project=project, user=request.user.id, role='Member').exists():
        return True or project.owner == request.user

    return False

class IsCommentPostAllowed(permissions.BasePermission):
  """
  - project owners & members can post & view comments.
  - superusers can have all access.
  """

  def has_permission(self, request, view):
    # Allow superusers to have all access
    if request.user.is_superuser:
      return True

    task_id = view.kwargs.get('task_id')
    if not task_id:
      return False

    try:
      task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
      return False

    project = task.project

    # Allow project owners to post comments
    if project.owner == request.user:
      return True

    # Allow project members to post comments
    if ProjectMember.objects.filter(project=project, user=request.user).exists():
      return True

    return False
  
class IsCommentOwnerOrAdmin(permissions.BasePermission):
  """
  - Owner can edit or delete their comment
  - Admin members and project owners can delete comments
  - Superusers can have all access
  """

  def has_object_permission(self, request, view, obj):
    # Allow superusers to have all access
    if request.user.is_superuser:
        return True

    # Check if the object is a comment
    if isinstance(obj, Comments):
      task = obj.task
      project = task.project

      # Allow project members to view comments
      if request.method in permissions.SAFE_METHODS:
        return ProjectMember.objects.filter(project=project, user=request.user).exists()

      # Allow comment owner to edit or delete their comment
      if obj.user == request.user:
        return True

      # Allow project owner and admin members to delete comments
      if request.method == 'DELETE':
        if project.owner == request.user:
          return True
        if ProjectMember.objects.filter(project=project, user=request.user, role='Admin').exists():
          return True

    return False
