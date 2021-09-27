from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import IndexUserCreationForm
from users.models import CustomUser

def index(request):
    title = 'Register and Smash Your Goals!'
    if request.method == "POST":
        form = IndexUserCreationForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            email_check = CustomUser.objects.filter(email=form.instance.email)
            if email_check.exists():
                messages.info(request, "An account already exists for that email address.")
            else:
                user = form.save()
                login(request, user)
                return redirect('home')

    form = IndexUserCreationForm(request.POST or None, request.FILES or None)
    return render(request, 'index.html', context={'form' : form, 'title': title})