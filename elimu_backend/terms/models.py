from django.db import models
from school.models import school


class Terms(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    term_name = models.IntegerField()
    opening_date = models.DateField()
    closing_date = models.DateField()

    class Meta:
        unique_together = [['school', 'opening_date'], ['school', 'closing_date']]
        verbose_name_plural = 'Terms'