from django.urls import path
from .views import CreateInstaPostView, UpdateInstaPostView, PostDetailView, \
    DeletePostView

urlpatterns = [
    path('create-post/', CreateInstaPostView.as_view(), name='create'),
    path('update/<uuid:pk>/', UpdateInstaPostView.as_view(), name='update'),
    path('detail/<uuid:pk>/', PostDetailView.as_view(), name='detail'),
    path('delete/<uuid:pk>/', DeletePostView.as_view(), name='delete'),
]
