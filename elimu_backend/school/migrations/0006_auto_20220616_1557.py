# Generated by Django 3.2.9 on 2022-06-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_school_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='mpesa_business_number',
        ),
        migrations.AddField(
            model_name='school',
            name='mpesa_till_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]