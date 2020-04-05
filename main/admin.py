from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'content',
        'author',
        'publish',
        'created',
        'updated',
        'status',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'article',
        'user',
        'body',
        'created',
    ]
