# Generated by Django 3.1.3 on 2021-10-30 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='streams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.IntegerField()),
                ('stream_name', models.CharField(max_length=15)),
                ('class_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teachers')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
            options={
                'verbose_name_plural': 'streams',
            },
        ),
    ]