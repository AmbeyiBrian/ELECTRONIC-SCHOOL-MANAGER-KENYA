# Generated by Django 3.2.9 on 2022-05-30 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0005_alter_school_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('target_audience', models.CharField(choices=[('All', 'All'), ('Teachers', 'Teachers'), ('Parents', 'Parents')], max_length=15)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('sms', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
    ]