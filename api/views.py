from user_post.models import Post
from api.serializers import PostSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from account.models import UserProfile
from rest_framework.decorators import action
from rest_framework.response import Response


class UserPostListViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    # @action(methods=['post'], detail=True, url_name='posts')
    # def user_profile_posts(self, request, pk=None):
    #     posts = Post.objects.filter(profile__owner=pk)
    #     serializer = self.get_serializer(posts, many=True)
    #     return Response(serializer.data)


class ProfileViewApi(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()

