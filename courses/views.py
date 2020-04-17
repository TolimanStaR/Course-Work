from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import render
from django.views.generic.list import ListView

from braces.views import GroupRequiredMixin

from .models import Course


# class ManageCourseListView(ListView):
#     model = Course
#     template_name = 'courses/manage/course/list.html'
#
#     def get_queryset(self):
#         qs = super(ManageCourseListView, self).get_queryset()
#         return qs.filter(owner=self.request.user.user_profile)


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user.user_profile)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user.user_profile
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview', ]
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    fields = ['subject', 'title', 'slug', 'overview', ]
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'


class CourseCreateView(GroupRequiredMixin,
                       OwnerCourseEditMixin,
                       CreateView, ):
    group_required = u"Instructor"


class CourseUpdateView(GroupRequiredMixin,
                       OwnerCourseEditMixin,
                       UpdateView, ):
    group_required = u'Instructor'


class CourseDeleteView(GroupRequiredMixin,
                       OwnerCourseMixin,
                       DeleteView, ):
    template_name = 'courses/manage/course/delete.html'
    success_url = reverse_lazy('manage_course_list')

    group_required = u'Instructor'
