from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views.generic import CreateView
from . forms import SignUpForm


class InstagramLoginView(LoginView):
    template_name = 'login_register.html'

    def form_valid(self, form):
        return HttpResponse('User logged in')


class InstagramSignupView(CreateView):
    form_class = SignUpForm
    template_name = 'login_register.html'

    def form_valid(self, form):
        return HttpResponse('User Registered Successfully!')
