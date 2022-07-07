from django.db import models
from school.models import school
from stream.models import streams


class timetable(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    stream = models.ForeignKey(streams, on_delete=models.CASCADE)
    lesson_number = models.IntegerField()
    subject = models.CharField(max_length=60)
    day = models.CharField(max_length=10)

    class Meta:
        unique_together = ['stream', 'lesson_number', 'day']
