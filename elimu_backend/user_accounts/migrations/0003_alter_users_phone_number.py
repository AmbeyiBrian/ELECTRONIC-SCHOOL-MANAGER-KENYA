# Generated by Django 3.2.9 on 2022-06-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0002_alter_users_user_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]