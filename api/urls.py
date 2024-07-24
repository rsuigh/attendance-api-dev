from django.urls import path, include
from .views import AttendanceRecorderListAPIView
from oauth2_provider import urls as oauth2_urls



urlpatterns = [
    path('attendance/', AttendanceRecorderListAPIView.as_view(), name='attendance_list'),
    path('o/', include(oauth2_urls)),


]
