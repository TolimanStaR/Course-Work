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
    about = models.TextField(blank=True, max_length=500)

    is_staff = models.BooleanField(default=False)

    RANG_CHOICES = (
        ("Новичок", "Новичок"),
        ("Лиманадек", "Лиманадек"),
        ("Черниговский батон", "Черниговский батон"),
        ("Сыр косичка", "Сыр косичка"),
        ("Масленок", "Масленок"),
        ("Советский for'ик", "Советский for'ик"),  # Exists, but never used
        ("Живой огурец", "Живой огурец"),
        ("Мафиозник", "Мафиозник"),
        ("Олимпиадник", "Олимпиадник"),
        ("Sensei", "Sensei"),
        ("Галактический кодер", "Галактический кодер"),
    )

    COLOR_CHOICES = (
        ('AAAAAA', 'AAAAAA'),
        ('6F72BE', '6F72BE'),
        ('7F9ED8', '7F9ED8'),
        ('7FBAD8', '7FBAD8'),
        ('88F8FF', '88F8FF'),
        ('00FFC5', '00FFC5'),
        ('1EFF88', '1EFF88'),
        ('F0FF00', 'F0FF00'),
        ('FFA600', 'FFA600'),
        ('FF6100', 'FF6100'),
        ('FF0000', 'FF0000'),
    )

    contest_rating = models.IntegerField(default=0)
    contest_rang = models.CharField(max_length=45, default=RANG_CHOICES[0][0], choices=RANG_CHOICES)
    contest_rang_color = models.CharField(default=COLOR_CHOICES[0][0], max_length=10, choices=COLOR_CHOICES)

    instructor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        ordering = ['-contest_rating']
