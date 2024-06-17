from django.db import models
from django.conf import settings



CLASS_TYPE_CHOICES = (
    ('an', 'Aula normal'),
    ('ar', 'Aula reposição'),
)


class AttendanceRecorder(models.Model):

    students_presents = models.TextField(
        null=True
    )

    date = models.DateField(
        verbose_name="Data da aula",
        blank=True,
        null=True
    )

    attendance = models.BooleanField(
        verbose_name="Presença do aluno",
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
