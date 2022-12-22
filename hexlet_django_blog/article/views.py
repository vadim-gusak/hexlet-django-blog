from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'article/article.html', context={'app_name': 'article'})
