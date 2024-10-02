from rest_framework import serializers
from .models import AttendanceRecorder
from datetime import date


class AttendanceRecorderSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceRecorder
        fields = '__all__'

    

    def validate(self, data):
        today = date.today()

        if data['date'] > today:
            raise serializers.ValidationError("Não é permitido enviar datas do futuro")

        if today.day <= 5:
            limit_date = date(today.year, today.month-1, 1)
        else:
            limit_date = date(today.year, today.month, 1)

        if data['date'] < limit_date:
            raise serializers.ValidationError("Não é permitido enviar datas referentes a um relatório anterior")

        return data



    
