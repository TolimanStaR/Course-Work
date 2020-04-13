from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )
    register_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)
    about = models.CharField(max_length=400, blank=True)

    RANG_CHOICES = (
        ("Новичек", "Новичек"),
        ("Лиманадек", "Лиманадек"),
        ("Черниговский батон", "Черниговский батон"),
        ("Сыр косичка", "Сыр косичка"),
        ("Масленок", "Масленок"),
        ("Простой советский forik", "Простой советский forik"),
        ("Живой огурец", "Живой огурец"),
        ("Мафиозник", "Мафиозник"),
        ("Олимпиадник", "Олимпиадник"),
        ("Sempai", "Sempai"),
        ("Sensei", "Sensei"),
        ("Галактический кодер", "Галактический кодер"),
    )

    contest_rating = models.PositiveIntegerField(default=0)
    contest_rang = models.CharField(max_length=45, default=RANG_CHOICES[0][0], choices=RANG_CHOICES)
    contest_rang_color = models.PositiveIntegerField(default=0xAAAAAA)

    def __str__(self):
        return f'[{self.contest_rang}] {self.user.username}'
