from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from .forms import SignUpForm
from .models import UserProfile
from django.shortcuts import render


class InstagramLoginView(LoginView, TemplateView):
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


    def get_form(self, form_class=form_class):
        
    def form_invalid(self, form):
        super().form_valid(form)
        return HttpResponse('Registration failed!!')
    
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse('User registration successful!!')
        
    def post(self, request, *args, **kwargs):
        if request.FILES:
            files = request.FILES
        else:
            files = None
        form = self.form_class(request.POST, files)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            bio = form.cleaned_data['bio']
            profile_pic = form.cleaned_data['profile_pic']
            profile = UserProfile.objects.create(user=user, bio=bio,
                                                 profile_pic=profile_pic)
            profile.save()
            return HttpResponse('User registration successful!!')
        else:
            return HttpResponse('Registration failed!!')


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


# class CreatePostView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post_creation.html'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
