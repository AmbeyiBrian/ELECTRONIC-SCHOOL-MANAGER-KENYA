# Generated by Django 3.2.9 on 2022-07-10 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0003_alter_users_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='national_id',
        ),
    ]
