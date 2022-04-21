from django.db import models
from school.models import school
from stream.models import streams
from teachers.models import teachers


class timetable(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    stream = models.ForeignKey(streams, on_delete=models.CASCADE)
    teacher = models.ForeignKey(teachers, on_delete=models.PROTECT)
    form = models.IntegerField(null=True)
    lesson_number = models.IntegerField()
    subject = models.CharField(max_length=20)
    day = models.CharField(max_length=10)

    class Meta:
        unique_together = ['lesson_number', 'day', 'stream']
