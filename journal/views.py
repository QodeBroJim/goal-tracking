from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import JournalEntryForm
from .models import Journal
from users.models import CustomUser


# display all of the user's journal entries
def journal_dashboard(request):
    journal_entries = Journal.objects.filter(author=request.user).order_by('-entry_date')
    context = {
        'journal_entries': journal_entries,
    }
    return render(request, 'journal/journal_dashboard.html', context)


# single journal entry
def journal(request, pk):
    journal = get_object_or_404(Journal, slug=pk)

    form = JournalEntryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.journal = journal
            form.save()
            return redirect(reverse('journal-detail', kwargs={
                'pk': pk
            }))
    context = {
        'form': form,
        'journal': journal,
    }
    return render(request, 'journal/journal.html', context)

# create journal entry
def journal_create(request):
    title = 'Create'
    instance = Journal(author=request.user)
    form = JournalEntryForm(instance=instance)
    #author = CustomUser.objects.filter(username=request.user.username)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST or None, 
                                request.FILES or None)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse('journal-detail', kwargs={
                'pk': form.instance.slug
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'journal/journal_create_form.html', context)

def journal_update(request, pk):
    title = 'Update'
    journal = get_object_or_404(Journal, pk=pk)
    form = JournalEntryForm(request.POST or None, request.FILES or None, instance=journal)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('journal-detail', kwargs={
                'pk': form.instance.slug
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'journal/journal_create_form.html', context)

def journal_delete(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    journal.delete()
    return redirect(reverse('journal-list'))

