from django.shortcuts import render
from .models import News
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def news_view(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})
