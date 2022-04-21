# Generated by Django 3.2.9 on 2022-04-18 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_school_logo'),
        ('subjects', '0004_electives'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electives',
            old_name='subject',
            new_name='subject_name',
        ),
        migrations.AlterUniqueTogether(
            name='electives',
            unique_together={('school', 'elective', 'subject_name')},
        ),
    ]
