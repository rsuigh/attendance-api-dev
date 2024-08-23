from rest_framework import serializers
from django.db.models import Count
from .models import AttendanceRecorder

class AttendanceRecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecorder
        fields = '__all__'