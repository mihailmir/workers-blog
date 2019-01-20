from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.contrib.auth import login, logout
from .forms import SignUpForm
from django.core.mail import send_mail


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.workers.name = form.cleaned_data.get('first_name')
            user.workers.surname = form.cleaned_data.get('last_name')
            user.workers.email = form.cleaned_data.get('email')
            if user.workers.image:
                user.workers.image = 'workers_list/photos/default_user.jpg'
            else:
                user.workers.image = form.cleaned_data.get('image')
            user.save()

            send_mail('Регистрация', f'Здравствуйете {user.username} вы успешно зарегестрировались на сайте учета сотрудников.',
                       'workerstestmail@gmail.com', [f'{user.workers.email}'], fail_silently=False)
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('/workers')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/workers')