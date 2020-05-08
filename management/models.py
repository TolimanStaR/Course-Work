from django.db import models
from django.utils import timezone


class TaskBase(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    input = models.TextField()
    output = models.TextField()
    time_limit = models.PositiveIntegerField(default=1)
    memory_limit = models.PositiveIntegerField()

    solved_by = models.IntegerField(default=0)

    solution = models.FileField(upload_to='code_files/')

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
        ('', ''),
    )

    difficulty = models.CharField(choices=DIFFICULT_CHOICES, default='a', max_length=3)

    class Meta:
        abstract = True

    def __str__(self):
        return f'Задача {self.pk}. {self.title}'


class SolutionCaseBase(models.Model):
    package_time = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=30, blank=True)
    task_file = models.FileField(upload_to='code_files/')
    task_code = models.TextField(default='#include <cheats>\n'
                                         'using namespace hack;\n'
                                         'int main () {\nchar input[];\n'
                                         'cin >> input;\n'
                                         'cout << hack::get_solution(input);\n'
                                         'return 0;\n'
                                         '}')
    verdict = models.CharField(max_length=150, default='Ожидается проверка')
    solved = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Default solution case'


class TestBase(models.Model):
    content = models.TextField()
    answer = models.TextField(default=None, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Default task test'
