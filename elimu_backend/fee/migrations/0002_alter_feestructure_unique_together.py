# Generated by Django 3.2.9 on 2022-05-08 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_school_logo'),
        ('fee', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feestructure',
            unique_together={('school', 'form', 'term', 'attribute')},
        ),
    ]