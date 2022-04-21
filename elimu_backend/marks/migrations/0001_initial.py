# Generated by Django 3.2.9 on 2022-02-18 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0005_alter_students_status'),
        ('school', '0005_alter_school_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('term', models.IntegerField()),
                ('mid_end', models.CharField(choices=[('Mid', 'Mid'), ('End', 'End')], default='Mid', max_length=5)),
                ('english_pp1', models.IntegerField(default=0)),
                ('english_pp2', models.IntegerField(default=0)),
                ('english_pp3', models.IntegerField(default=0)),
                ('kiswahili_pp1', models.IntegerField(default=0)),
                ('kiswahili_pp2', models.IntegerField(default=0)),
                ('kiswahili_pp3', models.IntegerField(default=0)),
                ('mathematics_pp1', models.IntegerField(default=0)),
                ('mathematics_pp2', models.IntegerField(default=0)),
                ('physics_pp1', models.IntegerField(default=0)),
                ('physics_pp2', models.IntegerField(default=0)),
                ('physics_pp3', models.IntegerField(default=0)),
                ('biology_pp1', models.IntegerField(default=0)),
                ('biology_pp2', models.IntegerField(default=0)),
                ('biology_pp3', models.IntegerField(default=0)),
                ('chemistry_pp1', models.IntegerField(default=0)),
                ('chemistry_pp2', models.IntegerField(default=0)),
                ('chemistry_pp3', models.IntegerField(default=0)),
                ('history_government_pp1', models.IntegerField(default=0)),
                ('history_government_pp2', models.IntegerField(default=0)),
                ('geography_pp1', models.IntegerField(default=0)),
                ('geography_pp2', models.IntegerField(default=0)),
                ('religion_pp1', models.IntegerField(default=0)),
                ('religion_pp2', models.IntegerField(default=0)),
                ('business_studies_pp1', models.IntegerField(default=0)),
                ('business_studies_pp2', models.IntegerField(default=0)),
                ('home_science_pp1', models.IntegerField(default=0)),
                ('home_science_pp2', models.IntegerField(default=0)),
                ('home_science_pp3', models.IntegerField(default=0)),
                ('agriculture_pp1', models.IntegerField(default=0)),
                ('agriculture_pp2', models.IntegerField(default=0)),
                ('computer_studies_pp1', models.IntegerField(default=0)),
                ('computer_studies_pp2', models.IntegerField(default=0)),
                ('music_pp1', models.IntegerField(default=0)),
                ('music_pp2', models.IntegerField(default=0)),
                ('art_design_pp1', models.IntegerField(default=0)),
                ('art_design_pp2', models.IntegerField(default=0)),
                ('aviation_pp1', models.IntegerField(default=0)),
                ('aviation_pp2', models.IntegerField(default=0)),
                ('electricity_pp1', models.IntegerField(default=0)),
                ('electricity_pp2', models.IntegerField(default=0)),
                ('power_mechanics_pp1', models.IntegerField(default=0)),
                ('power_mechanics_pp2', models.IntegerField(default=0)),
                ('wood_work_pp1', models.IntegerField(default=0)),
                ('wood_work_pp2', models.IntegerField(default=0)),
                ('french_pp1', models.IntegerField(default=0)),
                ('french_pp2', models.IntegerField(default=0)),
                ('german_pp1', models.IntegerField(default=0)),
                ('german_pp2', models.IntegerField(default=0)),
                ('arabic_pp1', models.IntegerField(default=0)),
                ('arabic_pp2', models.IntegerField(default=0)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.students')),
            ],
            options={
                'verbose_name_plural': 'Marks',
                'unique_together': {('school', 'student', 'term', 'mid_end')},
            },
        ),
    ]
