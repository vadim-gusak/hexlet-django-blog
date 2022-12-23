from django.urls import path
from hexlet_django_blog.my_classes import MyView

from hexlet_django_blog.article import views

urlpatterns = [
    path('', MyView.as_view()),
]
