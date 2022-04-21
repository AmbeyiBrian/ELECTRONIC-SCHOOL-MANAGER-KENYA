from django.db import models
from school.models import school
from stream.models import streams


class students(models.Model):
    school = models.ForeignKey(school, models.CASCADE)
    stream = models.ForeignKey(streams, models.PROTECT)
    admission_number = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    status = models.CharField(max_length=15, choices=[('Alumni', 'Alumni'), ('Discontinued', 'Discontinued'), ('Active', 'Active')])
    kcpe_marks = models.IntegerField()
    admission_date = models.DateField(auto_now=True)
    activation_code=models.CharField(max_length=10, null=True)
