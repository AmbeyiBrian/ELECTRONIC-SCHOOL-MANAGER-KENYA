from django.db import models
from school.models import school
from stream.models import streams
from user_accounts.models import Users


class students(models.Model):
    school = models.ForeignKey(school, models.CASCADE)
    stream = models.ForeignKey(streams, models.PROTECT)
    admission_number = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    status = models.CharField(max_length=15,
                              choices=[('Alumni', 'Alumni'), ('Discontinued', 'Discontinued'), ('Active', 'Active')])
    kcpe_marks = models.IntegerField()
    admission_date = models.DateField(auto_now_add=True)
    activation_code = models.CharField(max_length=10, null=True)
    parent = models.ForeignKey(Users, on_delete=models.PROTECT, null=True)

    subject_1 = models.CharField(max_length=30, null=True)
    subject_2 = models.CharField(max_length=30, null=True)
    subject_3 = models.CharField(max_length=30, null=True)
    subject_4 = models.CharField(max_length=30, null=True)
    subject_5 = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name_plural = 'Students'
        unique_together = ['first_name', 'last_name', 'school']

