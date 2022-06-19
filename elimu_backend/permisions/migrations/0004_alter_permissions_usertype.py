# Generated by Django 3.2.9 on 2022-06-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisions', '0003_alter_permissions_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='userType',
            field=models.CharField(choices=[('Deputy principal academics', 'Deputy principal academics'), ('Deputy principal administration', 'Deputy principal administration'), ('DoS', 'DoS'), ('Senior teacher', 'Senior teacher'), ('Class teacher', 'Class teacher'), ('Secretary', 'Secretary')], max_length=50),
        ),
    ]
