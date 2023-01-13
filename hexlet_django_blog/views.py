from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # return render(request, 'index.html', context={'who': 'World'})
        return redirect(reverse('article', kwargs={'tag': 'python', 'article_id': 42}))

def index(request):
    return render(request, 'index.html', context={'who': 'World'})


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(request, 'about.html', context={'tags': tags})
