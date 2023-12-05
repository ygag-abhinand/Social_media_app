from django.urls import path
from . views import InstagramLoginView, InstagramSignupView


urlpatterns = [
    path('', InstagramLoginView.as_view(), name='login'),
    path('signup/', InstagramSignupView.as_view(), name='signup'),
]
