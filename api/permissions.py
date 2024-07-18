from django.conf import settings
from rest_framework.permissions import BasePermission


class SafelistPermission(BasePermission):
    """
    Ensure the request's IP address is on the safe list configured in settings.

    '*' is allowed when DEBUG is set.
    """

    def has_permission(self, request, view):

        remote_addr = request.META['REMOTE_ADDR']

        # we may accept requests from anywhere during development
        if settings.DEBUG and '*' in settings.REST_SAFE_LIST_IPS:
            return True

        return False
