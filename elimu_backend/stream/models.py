from django.db import models
from school.models import school
from teachers.models import teachers


class streams(models.Model):
    school = models.ForeignKey(school, models.CASCADE)
    class_teacher = models.ForeignKey(teachers, models.CASCADE, null=True)
    form = models.IntegerField()
    stream_name = models.CharField(max_length=45)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'streams'

    def __str__(self):
        return '%s %s' % (self.form, self.stream_name)


class stream_subject_teacher(models.Model):
    school = models.ForeignKey(school, models.CASCADE)
    stream = models.ForeignKey(streams, models.CASCADE)
    teacher = models.ForeignKey(teachers, models.CASCADE)
    subject = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'stream subject teachers'

        unique_together = [['school', 'stream', 'teacher', 'subject'], ['school', 'stream','subject']]
