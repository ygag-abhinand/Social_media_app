from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    # password=
    # profile_pic = models.ImageField
    bio = models.TextField(blank=True)
    # followers = models
    # following = models
    # posts = models

    def __str__(self):
        return self.username
