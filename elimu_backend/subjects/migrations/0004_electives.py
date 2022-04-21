# Generated by Django 3.2.9 on 2022-04-18 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_school_logo'),
        ('subjects', '0003_auto_20220412_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='electives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elective', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)])),
                ('subject', models.CharField(max_length=20)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
            options={
                'unique_together': {('school', 'elective', 'subject')},
            },
        ),
    ]
