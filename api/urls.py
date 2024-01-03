from django.urls import path, include
from api.views import UserPostListViewSet, ProfileViewApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user_posts', UserPostListViewSet,
                basename='user_posts'),
router.register(r'profile', ProfileViewApi, basename='profile')
urlpatterns = [
    path('', include(router.urls)),
]

