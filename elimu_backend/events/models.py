from django.db import models
from school.models import school
from user_accounts.models import Users


class events(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    date_of_event = models.DateTimeField()
    title = models.CharField(max_length=200)
    event_description = models.CharField(max_length=1000)
    target_audience = models.CharField(max_length=30,
                                       choices=[('All', 'All'), ('Teachers', 'Teachers'), ('Parents', 'Parents')])
    creator=models.ForeignKey(Users, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.event_description, self.date_of_event)
