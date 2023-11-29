from django.urls import path
# from . views import InstagramLoginView, InstagramSignUpView
from .views import instagram_login

urlpatterns = [
    path('login/', instagram_login, name='login'),
    # path('signup/', InstagramSignUpView.as_view(), name='signup'),
]
