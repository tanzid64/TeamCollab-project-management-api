from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrIsSelf(BasePermission):
  """
  Custom permission to only allow users to edit their own details,
  but allow admin users to edit any user.
  """

  def has_permission(self, request, view):
    # Everyone can view, admins can do all
    if request.method in SAFE_METHODS or request.user.is_staff:
        return True

    # Non-admin users can only update/delete their own profile
    return view.action in ['retrieve', 'update', 'partial_update', 'destroy']

  def has_object_permission(self, request, view, obj):
    # Admins can do anything
    if request.user.is_staff:
        return True

    # Non-admin users can only update/delete their own profile
    return obj == request.user
