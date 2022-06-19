from django.db import models
from school.models import school
from students.models import students


class Marks(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE)
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    year = models.IntegerField()
    term = models.IntegerField()
    mid_end = models.CharField(max_length=5, default='Mid', choices=[('Mid', 'Mid'), ('End', 'End')])

    Eng_pp1 = models.IntegerField(default=0, null=True)
    Eng_pp2 = models.IntegerField(default=0, null=True)
    Eng_pp3 = models.IntegerField(default=0, null=True)

    Kis_pp1 = models.IntegerField(default=0, null=True)
    Kis_pp2 = models.IntegerField(default=0, null=True)
    Kis_pp3 = models.IntegerField(default=0, null=True)

    Mat_pp1 = models.IntegerField(default=0, null=True)
    Mat_pp2 = models.IntegerField(default=0, null=True)

    Phy_pp1 = models.IntegerField(default=0, null=True)
    Phy_pp2 = models.IntegerField(default=0, null=True)
    Phy_pp3 = models.IntegerField(default=0, null=True)

    Bio_pp1 = models.IntegerField(default=0, null=True)
    Bio_pp2 = models.IntegerField(default=0, null=True)
    Bio_pp3 = models.IntegerField(default=0, null=True)

    Chem_pp1 = models.IntegerField(default=0, null=True)
    Chem_pp2 = models.IntegerField(default=0, null=True)
    Chem_pp3 = models.IntegerField(default=0, null=True)

    Hist_pp1 = models.IntegerField(default=0, null=True)
    Hist_pp2 = models.IntegerField(default=0, null=True)

    Geo_pp1 = models.IntegerField(default=0, null=True)
    Geo_pp2 = models.IntegerField(default=0, null=True)

    RE_pp1 = models.IntegerField(default=0, null=True)
    RE_pp2 = models.IntegerField(default=0, null=True)

    BST_pp1 = models.IntegerField(default=0, null=True)
    BST_pp2 = models.IntegerField(default=0, null=True)

    Agri_pp1 = models.IntegerField(default=0, null=True)
    Agri_pp2 = models.IntegerField(default=0, null=True)

    HSC_pp1 = models.IntegerField(default=0, null=True)
    HSC_pp2 = models.IntegerField(default=0, null=True)
    HSC_pp3 = models.IntegerField(default=0, null=True)

    CST_pp1 = models.IntegerField(default=0, null=True)
    CST_pp2 = models.IntegerField(default=0, null=True)

    Music_pp1 = models.IntegerField(default=0, null=True)
    Music_pp2 = models.IntegerField(default=0, null=True)
    Music_pp3 = models.IntegerField(default=0, null=True)

    ArtDes_pp1 = models.IntegerField(default=0, null=True)
    ArtDes_pp2 = models.IntegerField(default=0, null=True)
    ArtDes_pp3 = models.IntegerField(default=0, null=True)

    Fre_pp1 = models.IntegerField(default=0, null=True)
    Fre_pp2 = models.IntegerField(default=0, null=True)
    Fre_pp3 = models.IntegerField(default=0, null=True)

    Ger_pp1 = models.IntegerField(default=0, null=True)
    Ger_pp2 = models.IntegerField(default=0, null=True)
    Ger_pp3 = models.IntegerField(default=0, null=True)

    Arabic_pp1 = models.IntegerField(default=0, null=True)
    Arabic_pp2 = models.IntegerField(default=0, null=True)
    Arabic_pp3 = models.IntegerField(default=0, null=True)

    WW_pp1 = models.IntegerField(default=0, null=True)
    WW_pp2 = models.IntegerField(default=0, null=True)
    WW_pp3 = models.IntegerField(default=0, null=True)

    Aviation_pp1 = models.IntegerField(default=0, null=True)
    Aviation_pp2 = models.IntegerField(default=0, null=True)
    Aviation_pp3 = models.IntegerField(default=0, null=True)

    Electricity_pp1 = models.IntegerField(default=0, null=True)
    Electricity_pp2 = models.IntegerField(default=0, null=True)
    Electricity_pp3 = models.IntegerField(default=0, null=True)

    PowMec_pp1 = models.IntegerField(default=0, null=True)
    PowMec_pp2 = models.IntegerField(default=0, null=True)
    PowMec_pp3 = models.IntegerField(default=0, null=True)

    MW_pp1 = models.IntegerField(default=0, null=True)
    MW_pp2 = models.IntegerField(default=0, null=True)
    MW_pp3 = models.IntegerField(default=0, null=True)

    BC_pp1 = models.IntegerField(default=0, null=True)
    BC_pp2 = models.IntegerField(default=0, null=True)
    BC_pp3 = models.IntegerField(default=0, null=True)

    KSL_pp1 = models.IntegerField(default=0, null=True)
    KSL_pp2 = models.IntegerField(default=0, null=True)
    KSL_pp3 = models.IntegerField(default=0, null=True)


    class Meta:
        unique_together = ['school', 'student', 'term', 'mid_end']
        verbose_name_plural = 'Marks'
