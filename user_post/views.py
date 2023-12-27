from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Like, Comment
from .forms import PostForm
from account.models import UserProfile
from django.urls import reverse_lazy
from account.utils.constants import ALL_FORMS_TEMPLATE
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.views import View


class CreateInstaPostView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = ALL_FORMS_TEMPLATE
    fields = ['media', 'caption']

    def form_valid(self, form):
        user = self.request.user
        profile = UserProfile.objects.get(owner=user)
        form.instance.profile = profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'create'
        return context

    def get_success_url(self):
        profile_pk = UserProfile.objects.get(owner=self.request.user).pk
        return reverse_lazy('profile', kwargs={'pk': profile_pk})


class UpdateInstaPostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = ALL_FORMS_TEMPLATE
    form_class = PostForm
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(profile__owner=user)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk':
                                            self.request.user.userprofile.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'update'
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'user_post/single_post.html'
    context_object_name = 'single_post'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        likes = Like.objects.filter(post=post)
        comments = Comment.objects.filter(post=post)
        liked_by_user = likes.filter(user=self.request.user).exists()
        context['likes'] = likes
        context['comments'] = comments
        context['liked_by_user'] = liked_by_user
        return context


class DeletePostView(LoginRequiredMixin, DeleteView):
    template_name = 'user_post/delete_confirmation.html'
    model = Post
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk':
                                            self.request.user.userprofile.pk})


class PostLikeView(LoginRequiredMixin, View):
    model = Like
    fields = []
    template_name = None

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(post_id=kwargs['pk'])
        is_liked = Like.objects.filter(post=post, user=request.user)
        if is_liked.exists():
            is_liked.delete()
        else:
            Like.objects.create(post=post, user=request.user)
        post.like_count()
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)
        else:
            return redirect('default_url_name')


class PostCommentView(LoginRequiredMixin, View):
    model = Comment
    fields = []
    template_name = None

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(post_id=kwargs['pk'])
        user_comment = request.POST.get('comment_text')
        Comment.objects.create(post=post, user=request.user,
                               text=user_comment)
        post.comment_count()
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)
        else:
            return redirect('default_url_name')

