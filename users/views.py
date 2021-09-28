from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from goals.models import Goal

def get_profile(user):
    profile = CustomUser.objects.filter(username=user.username)
    if profile.exists():
        return profile[0]
    return None

def register(request):
    title = 'Register and Start Smashing'
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            email_check = CustomUser.objects.filter(email=form.instance.email)
            if email_check.exists():
                messages.info(request, "An account already exists for that email address.")
            else:
                user = form.save()
                login(request, user)
                return redirect('home')

    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    
    return render(request, 'registration/register.html', context={'form' : form, 'title': title})

def profile(request):
    user = get_profile(request.user)
    goal = Goal.objects.filter(author=user, status='in-progress')
    context = {
        'user': user,
        'goal': goal,
    }
    return render(request, template_name='registration/profile.html', context=context)

def edit_user(request):
    title = 'Edit Your Profile'
    user = get_profile(request.user)
    form = CustomUserChangeForm(request.POST or None, request.FILES or None, instance=user)
    email = request.user.email
    if request.method == 'POST':
        if form.is_valid():
            form.instance.email = email
            form.save()
            return redirect(reverse('profile'))
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'registration/register.html', context)