from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'validate',}))
    avatar = forms.ImageField()

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'avatar',)

class CustomUserChangeForm(UserChangeForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'validate',}))
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'avatar',)