from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import models
from django.db.models import Count

from badgify.recipe import BaseRecipe
import badgify

from users.models import CustomUser

class FirstUser(BaseRecipe):
    name = 'Original User'
    slug = 'original-user'
    description = 'You were one of the first 200 users to start goal smashing!'

    @property
    def image(self):
        image = 'badges/og.jpg'
        return image

    @property
    def user_ids(self):
        user_list = CustomUser.objects.all().annotate(Count('email')).order_by('date_joined')[:200]
        return (user_list.values_list('id', flat=True))

badgify.register(FirstUser)
