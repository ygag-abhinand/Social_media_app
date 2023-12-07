from django.urls import path
from . views import InstagramLoginView, InstagramSignupView, profile, \
    edit_profile


urlpatterns = [
    path('', InstagramLoginView.as_view(), name='login'),
    path('signup/', InstagramSignupView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    path('edit/', edit_profile, name='edit-profile'),
]

