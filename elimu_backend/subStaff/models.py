from django.db import models
from user_accounts.models import Users
from school.models import school


class SubStaff(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sub_staff', null=True)
    activation_code = models.CharField(max_length=11)
    role = models.CharField(max_length=30)
