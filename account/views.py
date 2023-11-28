from django.contrib.auth.views import LoginView
from .models import UserProfile, Post
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View, CreateView
from .forms import LoginForm, SignUpForm, PostForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class InstagramLoginView(LoginView):
    template_name = 'login_register.html'
    # next_page =
    model = User
    # form_class = LoginForm

    def form_valid(self, form):
        return HttpResponse('User login Successful!')


class InstagramSignUpView(View):
    http_method_names = ['get', 'post']
    template_name = 'login_register.html'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.FILES:
            files = request.FILE
        else:
            files = None
        form = self.form_class(request.POST, files)
        if form.is_valid():
            user = form.save()
            bio = form.cleaned_data['bio']
            profile_pic = form.cleaned_data['profile_pic']
            profile = UserProfile.objects.create(user=user, bio=bio,
                                                 profile_pic=profile_pic)
            profile.save()
            return HttpResponse('User registration successful!!')
        else:
            return HttpResponse('Registration failed!!')


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_creation.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
