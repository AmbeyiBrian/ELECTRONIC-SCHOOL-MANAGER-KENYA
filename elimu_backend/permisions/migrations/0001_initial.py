# Generated by Django 3.2.9 on 2022-02-05 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0003_auto_20211116_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.CharField(choices=[('Deputy principal academics', 'Deputy principal academics'), ('Deputy principal administration', 'Deputy principal administration'), ('DoS', 'DoS'), ('Senior teacher', 'Senior teacher')], max_length=50)),
                ('update_timetable', models.BooleanField(default=False)),
                ('add_edit_stream', models.BooleanField(default=False)),
                ('add_edit_student', models.BooleanField(default=False)),
                ('create_event', models.BooleanField(default=False)),
                ('add_edit_teacher', models.BooleanField(default=False)),
                ('edit_school_info', models.BooleanField(default=False)),
                ('add_delete_gallery', models.BooleanField(default=False)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
    ]
