from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.db import models
from account.models import UserProfile
# from education.models import CourseTask, CourseTest

from management.models import TaskBase, TestBase
from management.fields import OrderField

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

import uuid

MAX_CHAR_LENGTH = 300


class Subject(models.Model):
    title = models.CharField(max_length=MAX_CHAR_LENGTH)
    slug = models.SlugField(max_length=MAX_CHAR_LENGTH, unique=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'


class Course(models.Model):
    owner = models.ForeignKey(UserProfile,
                              on_delete=models.DO_NOTHING,
                              related_name='courses_own',
                              )

    subject = models.ForeignKey(Subject,
                                on_delete=models.DO_NOTHING,
                                related_name='courses',
                                verbose_name='Предмет',
                                )

    students = models.ManyToManyField(UserProfile,
                                      related_name='courses',
                                      blank=True)

    title = models.CharField(max_length=MAX_CHAR_LENGTH, verbose_name='Название курса')
    slug = models.SlugField(max_length=MAX_CHAR_LENGTH, unique=True,
                            verbose_name='Уникальная ссылка. (Может содержать буквы латинского алфавита и тире)',
                            default=f'{str(uuid.uuid4())}')
    overview = models.TextField(verbose_name='Краткое описание курса', max_length=5000)
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

    title = models.CharField(max_length=MAX_CHAR_LENGTH, verbose_name='Название модуля')
    description = models.TextField(blank=True, verbose_name='Краткое описание модуля')
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Модуль {self.title} курса {self.course.title}'


class Content(models.Model):
    module = models.ForeignKey(Module,
                               on_delete=models.CASCADE,
                               related_name='contents',
                               )

    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={
                                         'model__in': (
                                             'text',
                                             'file',
                                             'image',
                                             'video',
                                             'code',
                                             # 'task',  Спойлер: Задачи будут, но позже
                                         )})

    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(
        UserProfile,
        related_name='%(class)s_related',
        on_delete=models.CASCADE,
    )

    item_title = models.CharField(max_length=MAX_CHAR_LENGTH,
                                  verbose_name='Название объекта. (Не отображается на странице модуля)')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def render(self):
        return render_to_string('courses/content/{}.html'.format(
            self._meta.model_name), {'item': self})

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.item_title}'


class Text(ItemBase):
    context = models.TextField(verbose_name='Текст')


class File(ItemBase):
    file = models.FileField(upload_to='files', verbose_name='Файл')


class Image(ItemBase):
    file = models.FileField(upload_to='images', verbose_name='Картинка')


class Video(ItemBase):
    url = models.URLField(verbose_name='Ссылка на видео (YouTube)')


class Code(ItemBase):
    code = models.TextField(verbose_name='Код')


# class Task(ItemBase, TaskBase):
#     pass
