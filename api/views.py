from django.shortcuts import render
from rest_framework import generics
from .models import AttendanceRecorder
from .serializers import AttendanceRecorderSerializer
from .permissions import SafelistPermission

class AttendanceRecorderListAPIView(generics.ListCreateAPIView):
    serializer_class = AttendanceRecorderSerializer
    permission_classes = [SafelistPermission]
    def get_queryset(self):
        queryset = AttendanceRecorder.objects.all()
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        return queryset

    
