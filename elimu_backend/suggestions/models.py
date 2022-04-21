from django.db import models
from user_accounts.models import Users
from school.models import school


class Suggestions(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    suggestion = models.TextField()
    date = models.DateTimeField(auto_now=True)
