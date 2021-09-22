from django.shortcuts import (  get_object_or_404, redirect, 
                                render, reverse)

from .forms import AffirmationForm
from .models import Affirmation


# display the user's affirmations sorted by goal and entry date
def affirmation_dashboard(request):
    affirmations = Affirmation.objects.filter(author=request.user).order_by('goal', '-entry_date')
    context = {
        'affirmations': affirmations,
    }
    return render(request, 'affirmations/affirmation_dashboard.html', context)

# single affirmation
def single_affirmation(request, pk):
    affirmation = get_object_or_404(Affirmation, url=pk)

    form = AffirmationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.affirmation = affirmation
            form.save()
            return redirect(reverse('affirmation-detail', kwargs={
                'pk': pk
            }))
    context = {
        'form': form,
        'affirmation': affirmation,
    }
    return render(request, 'affirmations/single_affirmation.html', context)

# create an affirmation
def affirmation_create(request):
    title = 'Create'
    instance = Affirmation(author=request.user)
    form = AffirmationForm(instance=instance)
    
    if request.method == 'POST':
        form = AffirmationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse('affirmation-detail', kwargs={
                'pk': form.instance.url
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'affirmations/affirmation_create_form.html', context)

# update an affirmation
def affirmation_update(request, pk):
    title = 'Update'
    affirmation = get_object_or_404(Affirmation, url=pk)
    form = AffirmationForm(request.POST or None, request.FILES or None, instance=affirmation)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('affirmation-detail', kwargs={
                'pk': form.instance.url
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'affirmations/affirmation_create_form.html', context)

# delete an affirmation
def affirmation_delete(request, pk):
    affirmation = get_object_or_404(Affirmation, url=pk)
    affirmation.delete()
    return redirect(reverse('affirmation-list'))