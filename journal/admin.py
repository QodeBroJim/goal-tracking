from django.contrib import admin

from .models import Journal

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'entry_date',)
    list_filter = ('entry_date',)
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-entry_date',)
