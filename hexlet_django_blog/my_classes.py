from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={'who': 'World'})


class MyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'article/article.html', context={'app_name': 'article'})
