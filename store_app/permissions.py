from rest_framework.permissions import BasePermission, SAFE_METHODS

class CustomPermission(BasePermission):
    """
    Custom permission to allow full access to authenticated users
    and read-only access to unauthenticated users.
    """
    def has_permission(self, request, view):
        # Allow read-only access for unauthenticated users
        if request.user and request.user.is_authenticated:
            return True
        elif request.method in SAFE_METHODS:
            # Allow GET, HEAD, OPTIONS requests for unauthenticated users
            return True
        else:
            # Deny write (POST, PUT, DELETE) requests for unauthenticated users
            return False
