# Generated by Django 3.2.9 on 2022-05-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0014_auto_20220427_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='CST_pp3',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
