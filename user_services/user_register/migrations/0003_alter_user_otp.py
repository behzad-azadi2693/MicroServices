# Generated by Django 4.0.5 on 2022-07-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0002_alter_user_is_active_alter_user_otp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]