from django.db import models
from user_accounts.models import Users
from random import choice


def activation_code_generator():
    s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    activation_code = ''
    for i in range(8):
        activation_code += choice(s)
    return activation_code


class school(models.Model):
    school_name = models.CharField(max_length=50, null=True)
    school_code = models.CharField(max_length=20, null=True)
    school_telephone = models.CharField(max_length=20, null=True)
    school_email = models.CharField(max_length=50, null=True)
    postal_address = models.CharField(max_length=20, null=True)
    postal_code = models.CharField(max_length=20, null=True)
    town = models.CharField(max_length=20, null=True)
    vision = models.CharField(max_length=200, null=True)
    mission = models.CharField(max_length=200, null=True)
    motto = models.CharField(max_length=200, null=True)
    logo = models.FileField(upload_to='school_logos', null=True)
    county = models.CharField(max_length=50, null=True)
    sub_county = models.CharField(max_length=50, null=True)
    bank_name = models.CharField(max_length=100, null=True)
    bank_account_number = models.CharField(max_length=100, null=True, default=174379)
    active = models.BooleanField(default=True)
    activation_code = models.CharField(max_length=12, default=activation_code_generator)
    creation_date=models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.school_name


class principal(models.Model):
    principal = models.OneToOneField(Users, on_delete=models.PROTECT, limit_choices_to={'user_class': 'Principal'},
                                     related_name='principal')
    school = models.OneToOneField(school, on_delete=models.PROTECT, related_name='school')

    class Meta:
        verbose_name_plural = 'Principals'

