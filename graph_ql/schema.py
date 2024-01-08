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


class PostCreateMutation(graphene.Mutation):
    class Arguments:
        caption = graphene.String(required=True)
        media = graphene.String(required=True)
        user_id = graphene.ID(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        caption = kwargs.get('caption')
        media = kwargs.get('media')
        user_id = kwargs.get('user_id')
        profile = UserProfile.objects.get(pk=user_id)
        post = Post(profile=profile, media=media, caption=caption)
        post.save()
        return PostCreateMutation(post=post)


class PostUpdateMutation(graphene.Mutation):
    class Arguments:
        caption = graphene.String()
        media = graphene.String()
        post_id = graphene.ID(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, caption, media, post_id):
        post = Post.objects.get(pk=post_id)
        if caption is not None:
            post.caption = caption
        if media is not None:
            post.media = media
        post.save()
        return PostUpdateMutation(post=post)


class PostDeleteMutation(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, post_id):
        post = Post.objects.get(pk=post_id)
        post.delete()
        return None


class CommentMutation(graphene.Mutation):
    class Arguments:
        post_id = graphene.String(required=True)
        text = graphene.String(required=True)
        user_id = graphene.ID(required=True)

    comment = graphene.Field(CommentType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        text = kwargs.get('text')
        post_id = kwargs.get('post_id')
        post = Post.objects.get(pk=post_id)
        user_id = kwargs.get('user_id')
        user = User.objects.get(pk=user_id)
        comment = Comment(user=user, post=post, text=text)
        comment.save()
        return CommentMutation(comment=comment)


class LikeMutation(graphene.Mutation):
    class Arguments:
        post_id = graphene.String(required=True)
        user_id = graphene.ID(required=True)

    like = graphene.Field(LikeType)

    @classmethod
    def mutate(cls, root, info, post_id, user_id):
        post = Post.objects.get(pk=post_id)
        user = User.objects.get(pk=user_id)
        like = Like(user=user, post=post)
        like.save()
        return LikeMutation(like=like)


class Mutation(graphene.ObjectType):
    post = PostCreateMutation.Field()
    post_update = PostUpdateMutation.Field()
    post_delete = PostDeleteMutation.Field()
    comment = CommentMutation.Field()
    like = LikeMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
# 7910c2ae-fb2f-4f7a-b4a2-ecc2cd9373eb
