# Generated by Django 3.2.9 on 2022-06-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fee', '0006_alter_feestatement_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feestatement',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]