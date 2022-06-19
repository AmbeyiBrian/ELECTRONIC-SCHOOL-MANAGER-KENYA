from django.db import models
from school.models import school
from students.models import students


class FeeStructure(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    form = models.IntegerField()
    term = models.IntegerField()
    attribute = models.CharField(max_length=50)
    amount = models.IntegerField()

    class Meta:
        unique_together = ['school', 'form', 'term', 'attribute']


class FeeStatement(models.Model):
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    amount = models.IntegerField()
    balance = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'ref_code', 'description', 'amount', 'balance', 'date']
