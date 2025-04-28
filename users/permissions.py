from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.userprofile.role == 'admin'
        )

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Always allow admin
        if request.user and request.user.userprofile.role == 'admin':
            return True
            
        # Check if the object has a user field
        if hasattr(obj, 'user'):
            return obj.user == request.user
            
        return False