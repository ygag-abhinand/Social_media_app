from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile
from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic']


class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=200, required=False)
    email = forms.EmailField()
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio',
                  'profile_pic']


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
