# Generated by Django 4.2.13 on 2024-07-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('students_attendance', models.JSONField(blank=True, default=None, max_length=5000, null=True)),
                ('date', models.DateField(blank=True, null=True, verbose_name='Data da aula')),
                ('class_type', models.CharField(blank=True, choices=[('an', 'Aula normal'), ('ar', 'Aula reposição')], max_length=2, null=True, verbose_name='Tipo de Aula')),
                ('course_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Id do curso')),
            ],
        ),
    ]
