from django.conf import settings
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class SafelistPermission(BasePermission):

    def has_permission(self, request, view):
        
        print(request.headers)