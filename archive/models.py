from django.db import models
from management.models import TaskBase, SolutionCaseBase, TestBase
from account.models import UserProfile

from django.utils import timezone


class ArchiveTask(TaskBase):
    added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-added',)

    def __str__(self):
        return f'{self.difficulty}. {self.title}'


class ArchiveTest(TestBase):
    task = models.ForeignKey(ArchiveTask, on_delete=models.CASCADE, related_name='tests')

    def __str__(self):
        return f'Тест задачи {self.task.title}'


class ArchiveSolutionCase(SolutionCaseBase):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='packages')
    task = models.ForeignKey(ArchiveTask, on_delete=models.CASCADE, related_name='packages')

    class Meta:
        ordering = ('-package_time',)

    def __str__(self):
        return f'Посылка {self.user.user.username} к задаче {self.task.title}'
