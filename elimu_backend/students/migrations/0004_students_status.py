# Generated by Django 3.2.9 on 2022-01-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_students_activation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='status',
            field=models.CharField(choices=[('Alumni', 'Alumni'), ('Discontinued', 'Discontinued'), ('Active', 'Active')], default='Active', max_length=15),
        ),
    ]