from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user or request.user.is_staff:
            return True
        else:
            raise PermissionDenied(detail="Вы не являетесь владельцем")

class IsModerator(BasePermission):
    message = 'Вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False