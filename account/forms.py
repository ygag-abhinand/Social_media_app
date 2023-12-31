from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic']


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, label="",
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Enter your User name'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Your email'}))
    password1 = forms.CharField(required=True, label="",
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'password'}))
    password2 = forms.CharField(required=True, label="",
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
