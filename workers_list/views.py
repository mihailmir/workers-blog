from django.shortcuts import render, redirect
from .models import Workers
from django.contrib.auth.decorators import login_required
from .forms import Edit


# Create your views here.


@login_required(login_url='/login')
def all_workers(request):
    workers = Workers.objects.all()
    return render(request, 'workers_list.html', {'work': workers})


@login_required(login_url='/login')
def profile(request, id):
    profile = Workers.objects.get(user_id=id)
    return render(request, 'profile.html', {'profile': profile, 'request': request}, )


def edit_fp(request):
    page = Workers.objects.get(user_id=request.user.id)
    form = Edit(request.POST or None, request.FILES or None, instance=page)
    context = {'form': form, 'profile': page}
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('workers')

    return render(request, 'edit.html', context)
