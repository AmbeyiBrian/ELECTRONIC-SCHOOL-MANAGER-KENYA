# Generated by Django 3.2.9 on 2022-04-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_school_logo'),
        ('subjects', '0002_alter_optional_subjects_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optional_subjects',
            name='group',
            field=models.IntegerField(choices=[(4, 4), (5, 5)]),
        ),
        migrations.AlterUniqueTogether(
            name='optional_subjects',
            unique_together={('school', 'group', 'subject_name')},
        ),
    ]
