from django.db import models
from user_accounts.models import Users
from school.models import school


class teachers(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='teacher', null=True)
    school = models.ForeignKey(school, on_delete=models.CASCADE, related_name='teachers')
    tsc_number = models.CharField(max_length=15)
    other_role = models.CharField(max_length=50)
    subject_1 = models.CharField(max_length=20)
    subject_2 = models.CharField(max_length=20)
    activation_code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.tsc_number
