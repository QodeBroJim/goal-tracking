from django.urls import path

from .views import (
    affirmation_dashboard, single_affirmation, affirmation_create, 
    affirmation_update, affirmation_delete
)

urlpatterns = [
    path('', affirmation_dashboard, name='affirmation-list'),
    path('affirmation/<pk>/', single_affirmation, name='affirmation-detail'),
    path('affirmation/<pk>/update/', affirmation_update, name='affirmation-update'),
    path('affirmation/<pk>/delete/', affirmation_delete, name='affirmation-delete'),
    path('create/', affirmation_create, name='affirmation-create'),

]