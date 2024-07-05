from django.core.management.base import BaseCommand
from api.models import AttendanceRecorder
from collections import defaultdict
import csv


class Command(BaseCommand):
    '''Export attendance data to CSV'''
    def handle(self, *args, **kwargs):
        attendance_records = AttendanceRecorder.objects.all()
        student_attendance = defaultdict(lambda: defaultdict(dict))
        dates_classes = set()
        for record in attendance_records:
            user = record.user
            date = record.date
            class_type = record.class_type
            for attendance in record.students_attendance:
                username = attendance["username"]
                present = attendance["present"]
                student_attendance[(user, username)][f"{date}+{class_type}"] = 1 if present else 0
                dates_classes.add(f"{date}+{class_type}")
        sorted_dates_classes = sorted(dates_classes)
        headers = ["user", "username"] + sorted_dates_classes
        with open('attendance_report.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            writer.writerow(headers)
            for (user_id, username), attendance in student_attendance.items():
                row = [user_id, username]
                for date_class in sorted_dates_classes:
                    row.append(attendance.get(date_class, 0))
                writer.writerow(row)