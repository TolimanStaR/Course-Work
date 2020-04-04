from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'content',
        'author',
        'publish',
        'created',
        'updated',
        'status'
    ]
