from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'register_date',
        'profile_image',
        'about',
        'contest_rating',
        'contest_rang',
        'contest_rang_color',
    ]
