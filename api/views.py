from django.shortcuts import render
from rest_framework import generics
from .models import AttendanceRecorder
from .serializers import AttendanceRecorderSerializer
from .permissions import SafelistPermission

class AttendanceRecorderListAPIView(generics.ListCreateAPIView):
    queryset = AttendanceRecorder.objects.all()
    serializer_class = AttendanceRecorderSerializer
    permission_classes = [SafelistPermission]


class AttendanceHistoryListAPIView(generics.ListCreateAPIView):
    serializer_class = AttendanceRecorderSerializer

    def get_queryset(self):
        queryset = AttendanceRecorder.objects.all()
        date = self.request.query_params.get('date', None)
        if name is not None:
            queryset = queryset.filter(date__icontains=name)
        return queryset
