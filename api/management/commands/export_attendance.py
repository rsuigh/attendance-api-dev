from django.core.management.base import BaseCommand
from api.models import AttendanceRecorder
from collections import defaultdict
import csv


class Command(BaseCommand):
    '''Export attendance data to CSV'''
    def handle(self, *args, **kwargs):
        records = []

        class_records = AttendanceRecorder.objects.all()

        students = set()
        dates = set()

        
        for record in class_records:
            dates.add(record.date)
            for attendance in record.students_attendance:
                students.add(attendance['username'])

        sorted_dates = sorted(dates)
        attendance_dict = defaultdict(lambda: {date: None for date in sorted_dates})


        for record in class_records:
            user = record.user
            date = record.date
            for attendance in record.students_attendance:
                attendance_dict[attendance['present']][date] = attendance['present']
                attendance_dict[attendance['username']]['user'] = user



    csv_filename = 'attendance.csv'
    with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Escrever o cabeçalho
            header = ['aluno', 'user'] + [f'data_{date}' for date in sorted_dates]
            writer.writerow(header)
            
            # Escrever os registros
            for student, attendance in attendance_dict.items():
                row = [student, attendance['user']] + [attendance[date] for date in sorted_dates]
                writer.writerow(row)