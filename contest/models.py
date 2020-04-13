from django.contrib.postgres.fields import ArrayField
from django.db import models

from management.models import TaskBase, SolutionCaseBase, TestBase
from account.models import UserProfile


class Contest(models.Model):
    starts_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=120)

    title = models.CharField(max_length=300)
    problem_set_size = models.PositiveIntegerField(default=1)

    active = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Раунд {self.pk}. {self.title}'


class ContestTask(TaskBase):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='tasks')

    number = models.PositiveIntegerField(default=1)


class ContestParticipant(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='participants')
    user = models.OneToOneField(UserProfile, on_delete=models.SET_DEFAULT, related_name='member', default=None)
    penalty = models.IntegerField(default=0)
    task_solved = models.PositiveIntegerField(default=0)
    stats = ArrayField(models.PositiveIntegerField(default=0), size=16, blank=True)

    class Meta:
        ordering = ('-task_solved', 'penalty')

    def __str__(self):
        return f'{self.user} - {self.contest.title}'


class ContestSolutionCase(SolutionCaseBase):
    participant = models.ForeignKey(ContestParticipant, on_delete=models.CASCADE, related_name='packages')
    task = models.ForeignKey(ContestTask, on_delete=models.CASCADE, related_name='packages')

    def __str__(self):
        return f'Посылка участника {self.participant.user.user.username}, ' \
               f'задача {self.task.title}, ' \
               f'вердикт: {self.verdict}'

    class Meta:
        ordering = ('-package_time',)


class ContestTest(TestBase):
    task = models.ForeignKey(ContestTask, on_delete=models.CASCADE, related_name='tests')

    def __str__(self):
        return f'Тест задачи {self.task.title}'
