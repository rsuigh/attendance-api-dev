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
        "id": 4,
        "user": null,
        "students_attendance": [
            {
                "present": false,
                "username": "aluno1"
            },
            {
                "present": true,
                "username": "aluno2"
            },
            {
                "present": false,
                "username": "aluno3"
            }
        ],
        "date": "2024-08-20",
        "class_type": "an",
        "course_id": "course-v1:SuirosProductions+C01+2024_T1"
    }
    '''
    created_at = models.DateTimeField(auto_now_add=True)

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
    

