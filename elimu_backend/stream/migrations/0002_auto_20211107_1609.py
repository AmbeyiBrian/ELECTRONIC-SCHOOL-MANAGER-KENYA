# Generated by Django 3.1.3 on 2021-11-07 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_auto_20211103_1506'),
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streams',
            name='class_teacher',
            field=models.ForeignKey(limit_choices_to={'user_class': 'Teacher'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teachers'),
        ),
    ]