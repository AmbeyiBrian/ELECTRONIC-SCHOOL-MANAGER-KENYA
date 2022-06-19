from django.db import models
from school.models import school
from user_accounts.models import Users


class Message(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    target_audience = models.CharField(max_length=15,choices=(('All', 'All'), ('Teachers', 'Teachers'),
                                                              ('Parents', 'Parents'), ('Sub staff', 'Sub staff')))
    date_time = models.DateTimeField(auto_now_add=True)
    sms = models.BooleanField()
    creator = models.ForeignKey(Users, on_delete=models.PROTECT)
