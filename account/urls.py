from django.urls import path
from . views import InstagramLoginView, InstagramSignUpView

urlpatterns = [
    path('login/', InstagramLoginView.as_view(), name='login'),
    path('signup/', InstagramSignUpView.as_view(), name='signup'),
]
