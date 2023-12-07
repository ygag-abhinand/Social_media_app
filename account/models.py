from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True,
                                    upload_to='profile_pic',
                                    default='user-default.png')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.owner.username




