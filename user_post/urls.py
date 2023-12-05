from django.urls import path
from .views import CreateInstaPostView, updateInstaPost

urlpatterns = [
    path('create-post/', CreateInstaPostView.as_view(), name='create'),
    path('update/<uuid:uuid>/', updateInstaPost, name='update'),
]
