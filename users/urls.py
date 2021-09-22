from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('register/', views.register, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.edit_user, name='user-update'),
]