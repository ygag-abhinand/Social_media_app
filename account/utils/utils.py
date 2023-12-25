from django.contrib.auth.models import User


def search_profiles(query):
    return User.objects.filter(username__icontains=query)

