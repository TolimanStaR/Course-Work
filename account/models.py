from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    register_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)
    about = models.CharField(max_length=400, blank=True)
    contest_rating = models.PositiveIntegerField(default=0)
    contest_rang = models.CharField(max_length=45, default='Начинающий')
    contest_rang_color = models.PositiveIntegerField(default=0xAAAAAA)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
