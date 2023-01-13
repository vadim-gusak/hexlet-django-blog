from django.urls import path
from hexlet_django_blog.article.views import MyView, article_view


urlpatterns = [
    path('', MyView.as_view()),
    path('<str:tag>/<article_id>', article_view, name='article')
]
