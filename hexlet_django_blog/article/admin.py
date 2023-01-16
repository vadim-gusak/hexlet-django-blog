from django.contrib import admin
from django.contrib.admin import DateFieldListFilter, AllValuesFieldListFilter
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']
    list_display = ('name', 'timestamp')
    list_filter = (('timestamp', DateFieldListFilter),('name', AllValuesFieldListFilter))
