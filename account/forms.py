from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile
from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'email', 'profile_pic']


class SignUpForm(UserCreationForm, ProfileForm):
    bio = forms.CharField(max_length=200)
    email = forms.EmailField()
    profile_pic = forms.ImageField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','bio',
                  'email', 'profile_pic']

    # profile = ProfileForm()


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
