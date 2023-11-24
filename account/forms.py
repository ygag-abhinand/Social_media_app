from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic']


class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio',
                  'profile_pic']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
