# Generated by Django 4.2.7 on 2023-11-27 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]