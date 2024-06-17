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

    students_attendance = models.JSONField(
        max_length=2000,
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
