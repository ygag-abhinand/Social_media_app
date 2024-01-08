from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
from account.models import UserProfile
from django.contrib.auth.models import User


# Create your models here.
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
        return self.caption

    def like_count(self):
        self.like_count = Like.objects.filter(post=self).count()
        self.save()


    def comment_count(self):
        self.comment_count = Comment.objects.filter(post=self).count()
        self.save()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.user, self.post)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return '{}:{}'.format(self.user, self.text)

