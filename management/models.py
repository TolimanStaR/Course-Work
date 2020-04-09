from django.db import models
from django.utils import timezone


class TaskBase(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    input = models.TextField()
    output = models.TextField()
    time_limit = models.PositiveIntegerField(default=1)
    memory_limit = models.PositiveIntegerField()

    solution = models.FileField(upload_to='code_files/')

    class Meta:
        abstract = True

    def __str__(self):
        return f'Задача {self.pk}. {self.title}'


class SolutionCaseBase(models.Model):
    package_time = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=30, blank=True)
    task_file = models.FileField(upload_to='code_files/')
    task_code = models.TextField(default='<Code>')
    verdict = models.CharField(max_length=150, default='Выполняется проверка')
    solved = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Default solution case'


class TestBase(models.Model):
    content = models.TextField()
    answer = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return 'Default task test'
