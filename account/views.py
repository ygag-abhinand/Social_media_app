from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import SignUpForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class InstagramLoginView(LoginView):
    template_name = 'account/login_register.html'

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse('User logged in!')

    def form_invalid(self, form):
        super().form_invalid(form)
        return HttpResponse('Sorry try again!!')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'login'
        return context


class InstagramSignupView(CreateView):
    template_name = 'account/login_register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'register'
        return context


    # def form_invalid(self, form):
    #     super().form_valid(form)
    #     return HttpResponse('Registration failed!!')
    #
    # def form_valid(self, form):
    #     super().form_valid(form)
    #     bio = form.cleaned_data.get('bio', '')
    #     profile_pic = form.cleaned_data.get('profile_pic', '')
    #     user = form.save(commit=False)
    #     user.save()
    #     profile = UserProfile.objects.create(owner=user, bio=bio,
    #                                          profile_pic=profile_pic)
    #     return HttpResponse('User registration successful!!')

