from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import uuid


class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.owner.username


class Post(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    media = models.FileField(validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp4', 'avi',
                            'mov'])])
    caption = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    post_id = models.UUIDField(default=uuid.uuid4, editable=False,
                               primary_key=True, unique=True)

    def __str__(self):
        return self.profile.owner.username
