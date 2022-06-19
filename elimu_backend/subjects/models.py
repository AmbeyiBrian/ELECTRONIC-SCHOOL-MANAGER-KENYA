from django.db import models
from school.models import school
from students.models import students


class optional_subjects(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    group = models.IntegerField(choices=[(4, 4), (5, 5)])
    subject_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ['school', 'group', 'subject_name']


class electives(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    elective = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    subject_name = models.CharField(max_length=20)

    class Meta:
        unique_together = ['school', 'elective', 'subject_name']


# class SubjectStudent(models.Model):
#     student = models.ForeignKey(students, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=30)
#
#     class Meta:
#         unique_together = ['student', 'subject']
