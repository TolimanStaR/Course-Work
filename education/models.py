from django.db import models

from management.models import TaskBase, SolutionCaseBase, TestBase

from account.models import UserProfile


class CourseTask(TaskBase):
    def __str__(self):
        return f'Учебная задача "{self.title}"'


class CourseSolutionCase(SolutionCaseBase):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='course_packages')
    task = models.ForeignKey(CourseTask, on_delete=models.CASCADE, related_name='course_packages')

    def __str__(self):
        return f'Тест к учебной задаче {self.task.title}'


class CourseTest(TestBase):
    task = models.ForeignKey(CourseTask, on_delete=models.CASCADE, related_name='tests')
