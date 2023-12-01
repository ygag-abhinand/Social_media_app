from django.urls import path
from . views import InstagramLoginView, InstagramSignupView, \
    CreateInstaPostView, updateInstaPost


urlpatterns = [
    path('login/', InstagramLoginView.as_view(), name='login'),
    path('signup/', InstagramSignupView.as_view(), name='signup'),
    path('create-post/', CreateInstaPostView.as_view(), name='create'),
    path('update/<str:pk>/', updateInstaPost, name='update'),
]
