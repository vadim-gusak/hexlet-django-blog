from django.urls import path
from hexlet_django_blog.my_classes import MyView


urlpatterns = [
    path('', MyView.as_view()),
]
