from django.db import models

from management.models import TaskBase, SolutionCaseBase

import datetime


class Contest(models.Model):
    start_time = models.DateTimeField()
    duration = models.DateTimeField(default=datetime.timedelta(hours=2))

    title = models.CharField(max_length=300)

    def __str__(self):
        return f'Раунд {self.pk + 1}. {self.title}'


class ContestTask(TaskBase):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='tasks')
