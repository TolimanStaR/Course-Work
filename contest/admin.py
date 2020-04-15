from django.contrib import admin
from .models import Contest, ContestTask, ContestParticipant, ContestSolutionCase, ContestTest, ContestPastParticipant


class ContestTaskInLine(admin.StackedInline):
    model = ContestTask
    extra = 2


class ContestTestInLine(admin.StackedInline):
    model = ContestTest
    extra = 1


class ContestParticipantInLine(admin.StackedInline):
    model = ContestParticipant


class ContestParticipantSolutionCaseInLine(admin.StackedInline):
    model = ContestSolutionCase
    extra = 3


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

    inlines = [
        ContestTaskInLine,
        ContestParticipantInLine,
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

    inlines = [ContestTestInLine]


@admin.register(ContestParticipant)
class ContestParticipantAdmin(admin.ModelAdmin):
    list_display = [
        'contest',
        'user',
        'task_solved',
        'penalty',
        'stats',
    ]

    # inlines = [
    #     ContestParticipantSolutionCaseInLine,
    # ]


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


@admin.register(ContestPastParticipant)
class ContestPastParticipantAdmin(admin.ModelAdmin):
    list_display = [
        'contest',
        'user',
        'penalty',
        'stats',
        'tasks_solved',
    ]
