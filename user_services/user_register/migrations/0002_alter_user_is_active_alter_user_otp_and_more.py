# Generated by Django 4.0.5 on 2022-07-12 15:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='user is active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.", regex='^\\+?1?\\d{11,11}$')], verbose_name='your phone number'),
        ),
    ]
