from django.db import models
from students.models import students


class attendanceSheet(models.Model):
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    year = models.IntegerField(default=2022)
    term = models.IntegerField(default=1)
    date = models.DateField()
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ['student', 'date']
