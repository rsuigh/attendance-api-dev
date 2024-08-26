from rest_framework import generics, permissions

from .models import AttendanceRecorder
from .serializers import AttendanceRecorderSerializer
from .permissions import SafelistPermission
from django.db.models import Subquery, OuterRef




class AttendanceRecorderListAPIView(generics.ListCreateAPIView):
    serializer_class = AttendanceRecorderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = AttendanceRecorder.objects.all()
        date = self.request.query_params.get('date', None)
        course_id = self.request.query_params.get('course_id', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        if course_id is not None:
            # the character "+", for some reason, disapear in url params
            queryset = queryset.filter(course_id=course_id.replace(" ","+"))

        # Subquery para pegar a última ocorrência de cada data
        subquery = queryset.filter(date=OuterRef('date')).order_by('-created_at').values('id')[:1]
        return queryset.filter(id__in=Subquery(subquery)).order_by('date')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        response = super().list(request, *args, **kwargs)
        
        # Calcular a porcentagem de presença usando o queryset filtrado
        attendance_percentage = self.calculate_attendance_percentage(queryset)
        response.data = {
            'attendance_records': response.data,
            'attendance_percentage': attendance_percentage
        }
        return response
    
    def calculate_attendance_percentage(self, queryset):
        attendance_count = {}
        total_classes = queryset.values('date').distinct().count()

        for record in queryset:
            for attendance in record.students_attendance:
                username = attendance['username']
                if username not in attendance_count:
                    attendance_count[username] = {'present': 0, 'total': 0}
                attendance_count[username]['total'] += 1
                if attendance['present']:
                    attendance_count[username]['present'] += 1

        attendance_percentage = {
            username: round((counts['present'] / total_classes) * 100, 1)
            for username, counts in attendance_count.items()
        }
        return attendance_percentage

    
