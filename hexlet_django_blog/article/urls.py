from django.urls import path
from hexlet_django_blog.article.views import MyView, ArticleView, ArticleFormCreateView


urlpatterns = [
    path('', MyView.as_view(), name='articles'),
    path('<int:id>', ArticleView.as_view(), name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='article_create'),
]
