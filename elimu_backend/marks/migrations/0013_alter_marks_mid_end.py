# Generated by Django 3.2.9 on 2022-04-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0012_auto_20220427_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='mid_end',
            field=models.CharField(choices=[('Mid', 'Mid'), ('End', 'End')], default='End', max_length=5),
        ),
    ]
