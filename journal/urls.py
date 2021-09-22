from django.urls import path

from .views import (
                    journal, journal_dashboard, journal_update, 
                    journal_delete, journal_create
                    )

urlpatterns = [
    path('', journal_dashboard, name='journal-list'),
    path('journal/<pk>/', journal, name='journal-detail'),
    path('journal/<pk>/update/', journal_update, name='journal-update'),
    path('journal/<pk>/delete/', journal_delete, name='journal-delete'),
    path('create/', journal_create, name='journal-create'),
]