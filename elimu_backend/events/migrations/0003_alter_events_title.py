# Generated by Django 3.2.9 on 2022-01-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
