from django.shortcuts import render
from rest_framework import generics
from .models import AttendanceRecorder
from .serializers import AttendanceRecorderSerializer

class AttendanceRecorderListAPIView(generics.ListCreateAPIView):
    queryset = AttendanceRecorder.objects.all()
    serializer_class = AttendanceRecorderSerializer

