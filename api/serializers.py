from rest_framework import serializers
from user_post.models import Post, Comment, Like
from django.contrib.humanize.templatetags import humanize
from account.models import UserProfile


class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['post_id', 'media', 'caption', 'created_at',
                  'profile', 'username', 'like_count', 'comment_count']

    def get_username(self, obj):
        return obj.profile.owner.username

    def get_created_at_humanized(self, obj):
        return humanize.naturaltime(obj.created_at)

    def get_like_count(self, obj):
        return Like.objects.filter(post=obj).count()

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['username', 'text']

    def get_username(self, obj):
        return obj.user.username


class ProfileSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'bio', 'owner', 'followers', 'following',
                  'post', 'comments']

    def get_post(self, obj):
        post = obj.post_set.all()
        serializers = PostSerializer(post, many=True)
        return serializers.data

    def get_comments(self, obj):
        comments = Comment.objects.filter(post__profile=obj)
        comment_serializer = CommentSerializer(comments, many=True)
        return comment_serializer.data

