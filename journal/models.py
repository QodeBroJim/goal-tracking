from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from goals.models import Goal

User = get_user_model()

class Journal(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='entry_date')
    entry_date = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField() # ckeditor
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('journal-detail', kwargs={
            'pk': self.slug
        })

    def get_update_url(self):
        return reverse('journal-update', kwargs={
            'pk': self.slug
        })

    def get_delete_url(self):
        return reverse('journal-delete', kwargs={
            'pk': self.slug
        })
