from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAdminUser

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            return IsAdminUser().has_permission(request, view)
        return False