from django import forms
from ckeditor.fields import RichTextFormField # imports CkEditor's form
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

from .models import Journal # imports the Journal model
from goals.models import Goal # imports the Goal model
from users.models import CustomUser # imports the custom user model from user's app

class JournalEntryForm(forms.ModelForm):
    content = RichTextFormField()
    slug = forms.CharField(label='Unique URL', 
                            required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Example: your-first-journal-entry'}))

    class Meta:
        model = Journal
        fields = ('title', 'slug', 'content', 'goal', 'author', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = CustomUser.objects.filter(username=get_current_user())
        self.fields['goal'].queryset = Goal.objects.filter(author=get_current_user())