from django import forms
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

from .models import Affirmation
from goals.models import Goal
from users.models import CustomUser

class AffirmationForm(forms.ModelForm):
    
    class Meta:
        model = Affirmation
        fields = (
            'affirmation', 'url', 'goal', 'author',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = CustomUser.objects.filter(username = get_current_user())
        self.fields['goal'].queryset = Goal.objects.filter(author = get_current_user())