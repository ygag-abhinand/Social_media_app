from .models import UserProfile, User
from django.db.models.signals import post_save


def create_user_profile(sender, created, instance, **kwargs):
    if created:
        user = instance
        UserProfile.objects.create(owner=user)


post_save.connect(create_user_profile, sender=User)
