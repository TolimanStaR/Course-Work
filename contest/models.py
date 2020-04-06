from django.contrib.postgres.fields import ArrayField
from django.db import models

from management.models import TaskBase, SolutionCaseBase, TestBase
from account.models import UserProfile

import datetime


class Contest(models.Model):
    starts_at = models.DateTimeField()
    duration = models.DateTimeField(default=datetime.timedelta(hours=2))

    title = models.CharField(max_length=300)
    problem_set_size = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Раунд {self.pk + 1}. {self.title}'


class ContestTask(TaskBase):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='tasks')

    DIFFICULT_CHOICES = (
        ('a', 'A'),
        ('b', 'B'),
        ('b1', 'B1'),
        ('b2', 'B2'),
        ('c', 'C'),
        ('c1', 'C1'),
        ('c2', 'C2'),
        ('d', 'D'),
        ('d1', 'D1'),
        ('d2', 'D2'),
        ('e', 'E'),
        ('e1', 'E1'),
        ('e2', 'E2'),
        ('f', 'F'),
        ('f1', 'F1'),
        ('f2', 'F2'),
        ('g', 'G'),
        ('h', 'H'),
        ('i', 'I'),
        ('j', 'J'),
        ('k', 'K'),
        ('l', 'L'),
    )

    difficulty = models.CharField(choices=DIFFICULT_CHOICES, default='a', max_length=3)


class ContestParticipant(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='participants')
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    penalty = models.IntegerField(default=0)
    task_solved = models.PositiveIntegerField(default=0)
    stats = ArrayField(models.BooleanField(default=None), size=16, default=list([None] * 16))

    class Meta:
        ordering = ('-task_solved', 'penalty')


class ContestSolutionCase(SolutionCaseBase):
    participant = models.OneToOneField(ContestParticipant, on_delete=models.CASCADE, related_name='packages')
    task = models.OneToOneField(ContestTask, on_delete=models.CASCADE, related_name='packages')

    def __str__(self):
        return f'Посылка участника {self.participant.user.user.username}, ' \
               f'задача {self.task.title}, ' \
               f'вердикт: {self.verdict}'
