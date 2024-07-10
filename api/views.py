from django.shortcuts import render
from rest_framework import generics
from .models import AttendanceRecorder
from .serializers import AttendanceRecorderSerializer
from .permissions import SafelistPermission

class AttendanceRecorderListAPIView(generics.ListCreateAPIView):
    queryset = AttendanceRecorder.objects.all()
    serializer_class = AttendanceRecorderSerializer
    permission_classes = [SafelistPermission]

