from django.contrib.auth.views import LoginView
from .models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from . forms import LoginForm, SignUpForm


class InstagramLoginView(LoginView):
    template_name = 'login_register.html'
    model = User
    form_class = LoginForm

    def form_valid(self, form):
        return HttpResponse('User login Successful!')


# class InstagramSignUpView(View):
#     template_name = 'login_register.html'
#     model = UserProfile
#     form_class =
