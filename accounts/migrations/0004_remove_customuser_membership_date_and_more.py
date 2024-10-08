# Generated by Django 5.1.1 on 2024-09-07 13:01

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_customuser_age_alter_customuser_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='membership_date',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile_number',
            field=models.CharField(max_length=11, unique=True, validators=[accounts.models.validate_mobile_number]),
        ),
    ]
