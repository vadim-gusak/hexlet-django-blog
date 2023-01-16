from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


class MyView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={'articles': articles})
        # return redirect(reverse('article', kwargs={'tag': 'python', 'article_id': 42}))


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={'article': article})


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'article/create.html', {'form': form})


# class CommentArticleView(View):
#
#     def get(self, request, *args, **kwargs):
#         form = CommentArticleForm()
#         return render(request, 'comment.html', {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = CommentArticleForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['comment']
#             comment = Comment(name=name)
#             comment.save()


# def article_view(request, tag, article_id):
#     return HttpResponse(f'Статья номер {article_id}. Тег {tag}.')
