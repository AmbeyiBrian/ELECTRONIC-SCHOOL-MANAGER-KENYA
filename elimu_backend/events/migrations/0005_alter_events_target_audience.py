# Generated by Django 3.2.9 on 2022-01-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_events_target_audience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='target_audience',
            field=models.CharField(choices=[('All', 'All'), ('Teachers', 'Teachers'), ('Parents', 'Parents')], max_length=30),
        ),
    ]
