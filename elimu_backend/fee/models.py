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


class MpesaCalls(models.Model):
    CheckoutRequestID = models.TextField()
    ResponseDescription = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'


class MpesaPayment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    reference = models.TextField()
    phone_number = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'
