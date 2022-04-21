from django.db import models
from school.models import school


class Gallery(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='school_gallerys')
    description = models.CharField(max_length
                                   =1000)
    date = models.DateTimeField(auto_now_add=True)
