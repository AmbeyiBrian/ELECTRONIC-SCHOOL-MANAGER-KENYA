# Generated by Django 3.2.9 on 2022-05-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancesheet',
            name='term',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='attendancesheet',
            name='year',
            field=models.IntegerField(default=2022),
        ),
    ]
