# Generated by Django 4.2.7 on 2023-12-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_userprofile_profile_pics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to='profile_pic'),
        ),
    ]
