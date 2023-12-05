from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import SignUpForm
from .models import UserProfile


class InstagramLoginView(LoginView):
    template_name = 'login.html'

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

