from django.urls import path, include
from .views import AttendanceRecorderListAPIView

urlpatterns = [
    path('attendance/', AttendanceRecorderListAPIView.as_view(), name='attendance_list'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]
