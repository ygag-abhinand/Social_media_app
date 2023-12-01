from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import SignUpForm, PostForm
from .models import UserProfile, Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class InstagramLoginView(LoginView):
    template_name = 'login_register.html'

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse('User logged in!')

    def form_invalid(self, form):
        super().form_invalid(form)
        return HttpResponse('Sorry try again!!')


class InstagramSignupView(CreateView):
    template_name = 'login_register.html'
    form_class = SignUpForm
    model = UserProfile
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        super().form_valid(form)
        return HttpResponse('Registration failed!!')

    def form_valid(self, form):
        super().form_valid(form)
        bio = form.cleaned_data.get('bio', '')
        profile_pic = form.cleaned_data.get('profile_pic', '')
        user = form.save(commit=False)
        user.save()
        profile = UserProfile.objects.create(owner=user, bio=bio,
                                             profile_pic=profile_pic)
        return HttpResponse('User registration successful!!')


class CreateInstaPostView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'login_register.html'
    fields = ['media', 'caption']
    success_url = '/login'

    def form_valid(self, form):
        super().form_valid(form)
        profile = self.request.user.userprofile
        form.instance.profile = profile
        return HttpResponse('Post is created')

    def form_invalid(self, form):
        super().form_invalid(form)
        return HttpResponse('Unsuccessful!!')


@login_required(login_url='login')
def updateInstaPost(request, pk):
    user = request.user
    profile = user.userprofile_set.get(owner=user)
    print(profile, '=========')
    post = profile.post_set.get(id=pk)
    return HttpResponse('Successful!!')
