# Generated by Django 3.2.9 on 2022-02-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestions',
            name='suggestion',
            field=models.TextField(),
        ),
    ]
