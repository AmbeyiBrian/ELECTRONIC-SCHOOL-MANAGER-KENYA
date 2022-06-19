# Generated by Django 3.2.9 on 2022-04-21 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_alter_teachers_options'),
        ('school', '0005_alter_school_logo'),
        ('stream', '0010_stream_subject_teacher'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stream_subject_teacher',
            unique_together={('school', 'stream', 'teacher', 'subject')},
        ),
    ]
