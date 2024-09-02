from rest_framework import serializers
from django.db.models import Count
from .models import AttendanceRecorder
from datetime import datetime, timedelta



class AttendanceRecorderSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceRecorder
        fields = '__all__'

    def validate(self, data):
        today = datetime.today().date()

        if today.day <= 5:
            previous_month = today - timedelta(days=today.day)
            if data['date'] < previous_month:
                raise serializers.ValidationError("Você só pode enviar datas do mês anterior.")
            
        elif data['date'] > today.date():
            raise serializers.ValidationError("Não é permitido enviar datas do futuro") 
            
        else:
            if data['date'].month < today.month and data['date'].year == today.year:
                raise serializers.ValidationError("Não é permitido enviar datas do mês anterior após o dia 5.")
            
        return data



    
