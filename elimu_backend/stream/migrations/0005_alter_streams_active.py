# Generated by Django 3.2.9 on 2022-01-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0004_streams_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streams',
            name='active',
            field=models.BooleanField(),
        ),
    ]
