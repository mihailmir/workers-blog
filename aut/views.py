from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.contrib.auth import login
from .forms import SignUpForm


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.workers.name = form.cleaned_data.get('name')
            user.workers.surname = form.cleaned_data.get('surname')
            user.workers.email = form.cleaned_data.get('email')
            user.workers.image = form.cleaned_data.get('image')
            user.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)

            return redirect('/workers')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


