from django.db import models
from django.conf import settings



CLASS_TYPE_CHOICES = (
    ('an', 'Aula normal'),
    ('ar', 'Aula reposição'),
)


class AttendanceRecorder(models.Model):
    '''
        API post example:
        {
            "id": 1,
            "user": 12345
            "students_attendance": [
                {
                    "fulano": "true"
                },
                {
                    "beltrano": "false"
                },
                {
                    "zezinho": "true"
                }
            ],
            "date": "2024-06-17",
            "attendance": null,
            "class_type": "an",
            "course_id": "course-v1:SuirosProductions+C01+2024_T1"
        }
        true = present
        false = not present
    '''

    user = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=None
    )

    students_attendance = models.JSONField(
        max_length=5000,
        null=True,
        blank=True,
        default=None  
    )

    date = models.DateField(
        verbose_name="Data da aula",
        blank=True,
        null=True
    )

    class_type = models.CharField(
        verbose_name="Tipo de Aula",
        choices=CLASS_TYPE_CHOICES,
        max_length=2,
        blank=True,
        null=True
    )

    course_id = models.CharField(
        verbose_name="Id do curso",
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user} - {self.date}"
    
    def student_attendence_presence(self):
        if not self.students_attendance:
            return {}
        
        total_classes = {}
        total_attendance = {}

        for entry in self.students_attendance:
            username = entry.get("username")
            present = entry.get("present", False)

            if username not in total_attendance:
                total_attendance[username] = 0
                total_classes[username] = 0

            total_classes += 1
            if present:
                total_attendance[username] += 1

        percentage = {
            username: (total_attendance[username] / total_classes[username]) * 100
            for username in total_attendance
        }

        return percentage
