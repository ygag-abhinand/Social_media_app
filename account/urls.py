from django.urls import path
from . views import InstagramLoginView, InstagramSignupView

urlpatterns = [
    path('login/', InstagramLoginView.as_view(), name='login'),
    path('signup/', InstagramSignupView.as_view(), name='signup'),
]
