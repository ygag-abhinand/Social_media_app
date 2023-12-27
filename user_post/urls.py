from django.urls import path
from .views import CreateInstaPostView, UpdateInstaPostView, PostDetailView, \
    DeletePostView, PostLikeView, PostCommentView

urlpatterns = [
    path('create-post/', CreateInstaPostView.as_view(), name='create'),
    path('update/<uuid:pk>/', UpdateInstaPostView.as_view(), name='update'),
    path('detail/<uuid:pk>/', PostDetailView.as_view(), name='detail'),
    path('delete/<uuid:pk>/', DeletePostView.as_view(), name='delete'),
    path('like/<uuid:pk>/', PostLikeView.as_view(), name='like'),
    path('comment/<uuid:pk>/', PostCommentView.as_view(), name='comment'),
]
