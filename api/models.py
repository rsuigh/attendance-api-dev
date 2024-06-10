from django.db import models
from django.conf import settings



USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

CLASS_TYPE_CHOICES = (
    ('an', 'Aula normal'),
    ('ar', 'Aula reposição'),
)


class AttendanceRecorder(models.Model):

    user = models.OneToOneField(
        USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE
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

    def __str__(self):
        return f"{self.user} - {self.date}"
