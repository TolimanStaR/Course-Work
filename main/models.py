from django.db import models
from django.utils import timezone

from account.models import UserProfile


class Article(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='user_articles',
    )

    STATUS_CHOICES = (
        ('moderated', 'Moderated'),
        ('published', 'Published'),
    )

    status = models.CharField(choices=STATUS_CHOICES, default='moderated', max_length=20)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Статья {self.title}'

    class Meta:
        ordering = ('-publish',)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (
            '-created',
        )

    def __str__(self):
        return f'Комментарий пользователя {self.user} под постом {self.article}'
