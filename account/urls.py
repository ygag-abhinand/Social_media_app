from django.urls import path
from . views import InstagramLoginView, InstagramSignupView, ProfileView, \
    ProfileEditView, InstagramLogoutView, HomeView


urlpatterns = [
    path('', InstagramLoginView.as_view(), name='login'),
    path('signup/', InstagramSignupView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('edit/', ProfileEditView.as_view(), name='edit-profile'),
    path('logout/', InstagramLogoutView.as_view(), name='log-out'),
    path('home/', HomeView.as_view(), name='home'),
]

