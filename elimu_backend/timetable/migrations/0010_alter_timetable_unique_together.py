# Generated by Django 3.2.9 on 2022-05-31 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0009_alter_timetable_subject'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together=set(),
        ),
    ]
