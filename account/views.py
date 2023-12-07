from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import SignUpForm, ProfileForm
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class InstagramLoginView(LoginView):
    template_name = 'all_forms.html'

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
    template_name = 'all_forms.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'register'
        return context


@login_required(login_url='login')
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(owner=user)
    return render(request, 'account/profile.html', {'user': user, 'profile':
        profile})


@login_required(login_url='login')
def edit_profile(request):
    profile = UserProfile.objects.get(owner=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'all_forms.html', {'form': form, 'page': 'edit'})

