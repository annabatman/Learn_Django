# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import News


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)
