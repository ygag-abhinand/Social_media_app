# Generated by Django 4.2.7 on 2023-12-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pics',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to='uploads/profile_pics'),
        ),
    ]
