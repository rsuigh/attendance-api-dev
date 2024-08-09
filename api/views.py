from rest_framework import generics, permissions

from .models import AttendanceRecorder
from .serializers import AttendanceRecorderSerializer
from .permissions import SafelistPermission



class AttendanceRecorderListAPIView(generics.ListCreateAPIView):
    serializer_class = AttendanceRecorderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = AttendanceRecorder.objects.all()
        date = self.request.query_params.get('date', None)
        course_id = self.request.query_params.get('course_id', None)
        print(course_id)
        # if date is not None:
        #     queryset = queryset.filter(date=date)
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    
