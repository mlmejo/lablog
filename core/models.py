from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    year_level = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()
    disabled = models.BooleanField(default=False)
