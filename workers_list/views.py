from django.shortcuts import render, redirect
from .models import Workers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .forms import Edit


# CBV example
class AllWorkers(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Workers
    template_name = 'workers_list.html'
    context_object_name = 'work'
    paginate_by = 5  # 5 items per page
    extra_context = {'nav_range': 3}


class Profile(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Workers
    template_name = 'profile.html'
    context_object_name = 'profile'


# FBV example
def edit_fp(request):
    page = Workers.objects.get(user_id=request.user.id)
    context = {'profile': page}
    if request.method == 'GET':
        form = Edit(instance=page)
        context.update({'form': form})
    if request.method == 'POST':
        form = Edit(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('workers', page=1)
        context.update({'form': form})

    return render(request, 'edit.html', context)
