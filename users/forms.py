from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'validate',}))
    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={'placeholder': 'validate',}))
    
    def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            self.fields['password1'].help_text = ''
            self.fields['password2'].help_text = ''
            self.fields['username'].help_text = ''

            self.fields['email'].label = ''
            self.fields['username'].label = ''
            self.fields['first_name'].label = ''
            self.fields['last_name'].label = ''
            self.fields['avatar'].label = ''
            self.fields['password1'].label = ''
            self.fields['password2'].label = ''

            self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
            self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
            self.fields['password1'].widget.attrs['placeholder'] = 'Pick a password'
            self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter your password'

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'avatar',)

class CustomUserChangeForm(UserChangeForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'validate',}))
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'avatar',)