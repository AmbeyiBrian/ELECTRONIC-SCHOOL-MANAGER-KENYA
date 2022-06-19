from django.db import models
from school.models import school


class Permissions(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    userType = models.CharField(max_length=50, choices=[('Deputy principal academics', 'Deputy principal academics'),
                                                        ('Deputy principal administration',
                                                         'Deputy principal administration'),
                                                        ('DoS', 'DoS'), ('Senior teacher', 'Senior teacher'),
                                                        ('Class teacher', 'Class teacher'), ('Secretary', 'Secretary')])
    update_timetable = models.BooleanField(default=False)
    add_edit_stream = models.BooleanField(default=False)
    add_edit_student = models.BooleanField(default=False)
    create_event = models.BooleanField(default=False)
    add_edit_teacher = models.BooleanField(default=False)
    edit_school_info = models.BooleanField(default=False)
    add_delete_gallery = models.BooleanField(default=False)
    create_message = models.BooleanField(default=False)
    read_suggestion_box = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Permissions'
        unique_together = ['school', 'userType']

    def __str__(self):
        return self.userType
