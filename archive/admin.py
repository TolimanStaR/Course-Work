from django.contrib import admin
from .models import ArchiveTask, ArchiveTest, ArchiveSolutionCase


class ArchiveTestInLine(admin.StackedInline):
    model = ArchiveTest
    extra = 1


@admin.register(ArchiveTask)
class ArchiveTaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'difficulty',
        'body',
        'input',
        'output',
        'time_limit',
        'memory_limit',
        'solution',
    ]

    inlines = [
        ArchiveTestInLine,
    ]
