from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views.generic import CreateView
from . forms import SignUpForm
from django.views.generic import View
from django.shortcuts import render
from .models import UserProfile


class InstagramLoginView(LoginView):
    template_name = 'login_register.html'

    def form_valid(self, form):
        return HttpResponse('User logged in')


class InstagramSignupView(View):
    http_method_names = ['get', 'post']
    form_class = SignUpForm
    template_name = 'login_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            bio = form.cleaned_data["bio"]
            profile_pic = form.cleaned_data['profile_pic']
            profile = UserProfile.objects.create(user=user,bio=bio,
                                   profile_pic=profile_pic)
            profile.save()
            return HttpResponse("success")
        else:
            print("form is not valid")

        return HttpResponse("")

    def form_valid(self, form):
        return HttpResponse('User Registered Successfully!')
