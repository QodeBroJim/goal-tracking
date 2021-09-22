from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as ugtl

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/')
    email = models.EmailField(ugtl('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_shortname(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email

