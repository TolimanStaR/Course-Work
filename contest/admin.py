from django.contrib import admin
from .models import Contest, ContestTask, ContestParticipant, ContestSolutionCase, ContestTest


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'starts_at',
        'duration_minutes',
        'problem_set_size',
        'active',
        'completed',
    ]


@admin.register(ContestTask)
class ContestTaskAdmin(admin.ModelAdmin):
    list_display = [
        'contest',
        'title',
        'difficulty',
        'body',
        'input',
        'output',
        'time_limit',
        'memory_limit',
        'solution',
    ]


@admin.register(ContestParticipant)
class ContestParticipantAdmin(admin.ModelAdmin):
    list_display = [
        'contest',
        'user',
        'task_solved',
        'penalty',
        'stats',
    ]


@admin.register(ContestSolutionCase)
class ContestSolutionCaseAdmin(admin.ModelAdmin):
    list_display = [
        'participant',
        'task',
        'task_file',
        'package_time',
        'verdict',
        'solved',
    ]


@admin.register(ContestTest)
class ContestTestAdmin(admin.ModelAdmin):
    list_display = [
        'task',
        'content',
        'answer',
    ]
