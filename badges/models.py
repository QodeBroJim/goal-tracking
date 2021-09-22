from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import models

from badgify.recipe import BaseRecipe
import badgify

from users.models import CustomUser

class FirstUser(BaseRecipe):
    name = 'Original User'
    slug = 'original-user'
    description = 'You were one of the first 200 users to start goal smashing!'

    @property
    def image(self):
        return staticfiles_storage.open('og.jpg')

    @property
    def user_ids(self):
        if CustomUser.objects.filter(id<=200):
            return (CustomUser.objects.all().values_list('id', flat=True))
