from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, \
    TemplateView
from .forms import SignUpForm, ProfileForm
from .models import UserProfile
from django.shortcuts import render, redirect
from user_post.models import Post
from .utils.constants import ALL_FORMS_TEMPLATE
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from account.utils.utils import search_profiles
from user_post.models import Like, Comment


class InstagramLoginView(LoginView):
    template_name = ALL_FORMS_TEMPLATE

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Login failed. Please check your '
                                     'credentials.')
        return response

    def form_valid(self, form):
        super().form_valid(form)
        profile_id = self.request.user.userprofile.id
        next_page = reverse("profile", kwargs={'pk': profile_id})
        return HttpResponseRedirect(next_page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'login'
        return context


class InstagramLogoutView(LogoutView):
    next_page = 'login'


class InstagramSignupView(CreateView):
    template_name = ALL_FORMS_TEMPLATE
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'register'
        return context


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'account/profile.html'
    model = UserProfile
    pk_url_kwarg = 'pk'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        viewed_user_profile = self.object
        is_following = viewed_user_profile.followers.filter(
            pk=self.request.user.pk).exists()
        context['is_following'] = is_following
        context[
            'is_own_profile'] = viewed_user_profile.owner == self.request.user
        posts = self.object.post_set.all()
        context['posts'] = posts
        return context

    def post(self, request, *args, **kwargs):
        viewed_user_profile = self.get_object()
        is_following = viewed_user_profile.followers.filter(
            pk=request.user.pk).exists()
        if is_following:
            viewed_user_profile.followers.remove(request.user)
            request.user.userprofile.following.remove(
                viewed_user_profile.owner)
        else:
            viewed_user_profile.followers.add(request.user)
            request.user.userprofile.following.add(
                viewed_user_profile.owner)
        viewed_user_profile.update_follow_counts()
        return redirect('profile', pk=viewed_user_profile.pk)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = ALL_FORMS_TEMPLATE
    model = UserProfile
    context_object_name = 'form'

    def get_object(self, queryset=None):
        return self.model.objects.get(owner=self.request.user)

    def form_valid(self, form):
        form.save()
        return redirect('profile', pk=self.object.pk)

    def form_invalid(self, form):
        return render(self.request, self.template_name,
                      {'form': form, 'page': 'edit'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'edit'
        return context


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'account/home.html'

    def get(self, request, *args, **kwargs):
        page = 'feed'
        user_profile = UserProfile.objects.get(owner=request.user)
        following_users = user_profile.following.all()
        posts = Post.objects.filter(
            profile__owner__in=following_users).exclude(
            profile__owner=user_profile.owner).order_by(
            '-created_at')
        feeds = []
        for post in posts:
            liked_by_user = Like.objects.filter(
                post=post, user=request.user
            ).exists()
            comments = Comment.objects.filter(post=post)
            feed_item = {'owner_profile': post.profile.owner, 'post': post,
                         'liked_by_user': liked_by_user, 'comments': comments}
            feeds.append(feed_item)
        search_query = request.GET.get('search', '')
        if search_query:
            searched_profiles = search_profiles(search_query)
            page = 'search'
        else:
            searched_profiles = None
        context = {'feeds': feeds, 'searched_profiles': searched_profiles,
                   'page': page}
        return render(request, self.template_name, context)

