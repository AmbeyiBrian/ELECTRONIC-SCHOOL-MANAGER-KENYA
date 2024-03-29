# Generated by Django 3.2.9 on 2022-06-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0012_alter_stream_subject_teacher_unique_together'),
        ('timetable', '0013_alter_timetable_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together={('stream', 'lesson_number', 'day')},
        ),
    ]
