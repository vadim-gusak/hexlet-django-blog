from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views import View


class MyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'article/article.html', context={'app_name': 'hexlet_django_blog.article'})
        # return redirect(reverse('article', kwargs={'tag': 'python', 'article_id': 42}))

def article_view(request, tag, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tag}.')
