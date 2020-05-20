from django.contrib import admin
from .models import Subject, Course, Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


class ModuleInLine(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'subject',
        'created',
        'pk',
    ]
    list_filter = [
        'subject',
    ]
    search_fields = [
        'title',
        'overview',
    ]
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ModuleInLine,
    ]
