from django.conf import settings
from django.contrib.auth import login

from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class SafelistPermission(BasePermission):

    # def has_permission(self, request, view):
    #     token = request.GET.get('token')
    #     if token:
    #         try:
    #             access_token = AccessToken.objects.get(token=token)
    #             user = access_token.user
    #             login(request, user)
    #             return True
    #         except AccessToken.DoesNotExist:
    #             return False
    #     return False
    pass
            