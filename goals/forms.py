from django import forms
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

from .models import Category, Goal, Task
from users.models import CustomUser



class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('title', 'url', 'description', 'author')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = CustomUser.objects.filter(email=get_current_user())


class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = (
            'target_date', 'start_date', 'end_date', 'goal', 'url',
            'specific', 'measurable', 'achievable', 'relevant',
            'timely', 'category', 'status', 'author',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = CustomUser.objects.filter(email = get_current_user())
        self.fields['goal'].queryset = Goal.objects.filter(author = get_current_user())
        self.fields['category'].queryset = Category.objects.filter(author = get_current_user())

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task', 'url', 'due', 'description', 'completed', 'goal', 'author')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = CustomUser.objects.filter(email = get_current_user())
        self.fields['goal'].queryset = Goal.objects.filter(author = get_current_user())
        