from django.db import models
from account.models import UserProfile

MAX_CHAR_LENGTH = 300


class Subject(models.Model):
    title = models.CharField(max_length=MAX_CHAR_LENGTH)
    slug = models.SlugField(max_length=MAX_CHAR_LENGTH, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'Предмет {self.title}'


class Course(models.Model):
    owner = models.ForeignKey(UserProfile,
                              on_delete=models.DO_NOTHING,
                              related_name='courses_own',
                              )

    subject = models.ForeignKey(Subject,
                                on_delete=models.DO_NOTHING,
                                related_name='courses',
                                )

    title = models.CharField(max_length=MAX_CHAR_LENGTH)
    slug = models.SlugField(max_length=MAX_CHAR_LENGTH, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Курс {self.title}'


class Module(models.Model):
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='modules',
                               )

    title = models.CharField(max_length=MAX_CHAR_LENGTH)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Модуль {self.title} курса {self.course.title}'
