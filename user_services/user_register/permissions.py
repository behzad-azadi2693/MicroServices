
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class CheckSessionForNumbser(BasePermission):
    def has_permission(self, request, view):
        if request.session.get('phone_number', None) is None:
            return False
        return True