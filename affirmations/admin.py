from django.contrib import admin

from .models import Affirmation

@admin.register(Affirmation)
class AffirmationAdmin(admin.ModelAdmin):
    list_display = ('author', 'affirmation', 'entry_date',)
    list_filter = ('author', 'entry_date',)
    search_fields = ('affirmation', 'author',)
    prepopulated_fields = {'url': ('affirmation',)}
    ordering = ('author', '-entry_date',)