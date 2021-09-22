from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from goals.models import Goal

User = get_user_model()

class Affirmation(models.Model):
    affirmation = models.CharField(max_length=250)
    url = models.SlugField(max_length=250, unique_for_date='entry_date')
    entry_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return self.affirmation

    def get_absolute_url(self):
        return reverse('affirmation-detail', kwargs={
            'pk': self.url
        })

    def get_update_url(self):
        return reverse('affirmation-update', kwargs={
            'pk': self.url
        })

    def get_delete_url(self):
        return reverse('affirmation-delete', kwargs={
            'pk': self.url
        })
