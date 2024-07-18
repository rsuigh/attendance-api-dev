from django.urls import path
from .views import AttendanceRecorderListAPIView, AttendanceHistoryListAPIView

urlpatterns = [
    path('attendance/', AttendanceRecorderListAPIView.as_view(), name='attendance_list'),
]
