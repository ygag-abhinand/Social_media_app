import graphene
from graphene_django import DjangoObjectType
from user_post.models import Post, Like, Comment
from account.models import UserProfile
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username')


class ProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = '__all__'

    followers_count = graphene.Int()
    following_count = graphene.Int()

    def resolve_followers_count(self, info):
        return self.followers.count()

    def resolve_following_count(self, info):
        return self.following.count()


class LikeType(DjangoObjectType):
    class Meta:
        model = Like
        fields = '__all__'


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = '__all__'


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'
    user = graphene.Field(ProfileType)
    like_count = graphene.Int()
    comment_count = graphene.Int()
    comments = graphene.List(CommentType)


    def resolve_like_count(self, info):
        return Like.objects.filter(post=self).count()

    def resolve_comment_count(self, info):
        return Comment.objects.filter(post=self).count()
    def resolve_comments(self, info):
        return Comment.objects.filter(post=self)

    def resolve_followers_count(self, info):
        return self.post.count()

    def resolve_following_count(self, info):
        return self.following.count()


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType, user_id=graphene.ID())
    user_posts = graphene.List(PostType, user_id=graphene.ID())
    user_profile = graphene.Field(ProfileType, user_id=graphene.ID())

    def resolve_all_posts(root, info, user_id):
        return Post.objects.exclude(profile__in=user_id)

    def resolve_user_profile(root, info, user_id):
        return UserProfile.objects.get(pk=user_id)

    def resolve_user_posts(self, info, user_id):
        return Post.objects.filter(profile__in=user_id)


schema = graphene.Schema(query=Query)
