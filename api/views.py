from rest_framework import generics, permissions
from collections import defaultdict
from datetime import datetime
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
        
        # Obter as datas da primeira presença ou falta de cada aluno
        enrollment_dates = self.get_first_appearance_dates(queryset)
        
        # Calcular a porcentagem de presença usando o queryset filtrado
        attendance_percentage = self.calculate_attendance_percentage(queryset, enrollment_dates)
        response.data = {
            'attendance_records': response.data,
            'attendance_percentage': attendance_percentage
        }
        return response
    
    def get_first_appearance_dates(self, queryset):
        # Inicializa um dicionário para armazenar a primeira data de cada aluno
        first_appearance_dates = {}
        
        # Itera sobre o queryset para encontrar a primeira aparição de cada aluno
        for record in queryset:
            record_date = record.date
            for attendance in record.students_attendance:
                username = attendance['username']
                if username not in first_appearance_dates:
                    first_appearance_dates[username] = record_date
        
        return first_appearance_dates
    
    def calculate_attendance_percentage(self, queryset, enrollment_dates):
        attendance_count = defaultdict(lambda: {'present': 0, 'total_classes': 0, 'replacement': 0})
        # Processa os registros para contagem
        for record in queryset:
            record_date = record.date
            for attendance in record.students_attendance:
                username = attendance['username']
                enrollment_date = enrollment_dates.get(username)
                
                if enrollment_date and record_date >= enrollment_date:
                    if record.class_type == 'an':
                        attendance_count[username]['total_classes'] += 1
                        if attendance['present']:
                            attendance_count[username]['present'] += 1
                    elif record.class_type == 'ar':
                        if attendance['present'] and attendance_count[username]['replacement'] \
                                +attendance_count[username]['present'] < attendance_count[username]['total_classes']:
                            attendance_count[username]['replacement'] += 1
        # Calcula a porcentagem de presença
        
        attendance_percentage = {}

        for username, counts in attendance_count.items():
            # Soma presenças normais e de reposição
            total_presences = counts['present'] + counts['replacement']
            # Calcula a porcentagem de presença
            percentage = round((total_presences / max(counts['total_classes'], 1)) * 100, 1)
            # Armazena o resultado no dicionário
            attendance_percentage[username] = percentage
        
        return attendance_percentage

    
