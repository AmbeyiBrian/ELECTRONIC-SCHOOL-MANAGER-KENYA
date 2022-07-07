from django.db import models
from school.models import school
from students.models import students


class Marks(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    year = models.IntegerField()
    term = models.IntegerField()
    mid_end = models.CharField(max_length=5, default='Mid', choices=[('Mid', 'Mid'), ('End', 'End')])

    Eng = models.IntegerField(default=0, null=True)
    Kis = models.IntegerField(default=0, null=True)
    Mat = models.IntegerField(default=0, null=True)
    Phy = models.IntegerField(default=0, null=True)
    Bio = models.IntegerField(default=0, null=True)
    Chem = models.IntegerField(default=0, null=True)
    Hist = models.IntegerField(default=0, null=True)
    Geo = models.IntegerField(default=0, null=True)
    RE = models.IntegerField(default=0, null=True)
    BST = models.IntegerField(default=0, null=True)
    Agri = models.IntegerField(default=0, null=True)
    HSC = models.IntegerField(default=0, null=True)
    CST = models.IntegerField(default=0, null=True)
    Music = models.IntegerField(default=0, null=True)
    ArtDes = models.IntegerField(default=0, null=True)
    Fre = models.IntegerField(default=0, null=True)
    Ger = models.IntegerField(default=0, null=True)
    Arabic = models.IntegerField(default=0, null=True)
    WW = models.IntegerField(default=0, null=True)
    Aviation = models.IntegerField(default=0, null=True)
    Electricity = models.IntegerField(default=0, null=True)
    PowMec = models.IntegerField(default=0, null=True)
    MW = models.IntegerField(default=0, null=True)
    BC = models.IntegerField(default=0, null=True)
    KSL = models.IntegerField(default=0, null=True)


    class Meta:
        unique_together = ['school', 'student', 'term', 'mid_end']
        verbose_name_plural = 'Marks'
