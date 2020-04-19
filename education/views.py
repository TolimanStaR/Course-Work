from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView

from courses.models import Subject, Course

from .forms import CourseSubscribeForm


class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'courses/course/list.html'

    def get(self, request, subject=None):
        subjects = Subject.objects.annotate(
            total_courses=Count('courses')
        )
        courses = Course.objects.annotate(total_modules=Count('modules'))

        if subject:
            subject = get_object_or_404(Subject, slug=subject)
            courses = courses.filter(subject=subject)

        return self.render_to_response({'subjects': subjects,
                                        'subject': subject,
                                        'courses': courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)

        context['subscribe_form'] = CourseSubscribeForm(initial={'course': self.object})
        context['is_subscribed'] = False

        if self.object in [self.request.user.user_profile.courses]:
            context['is_subscribed'] = True

        return context


class UserSubscribeCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseSubscribeForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user.user_profile)
        return super(UserSubscribeCourseView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_course_detail', args=[self.course.id])


class UserCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'users/course/list.html'

    def get_queryset(self):
        qs = super(UserCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user.user_profile])


class UserCourseDetailView(DetailView):
    model = Course
    template_name = 'users/course/detail.html'

    def get_queryset(self):
        qs = super(UserCourseDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user.user_profile])

    def get_context_data(self, **kwargs):
        context = super(UserCourseDetailView, self).get_context_data(**kwargs)
        course = self.get_object()

        if 'module_id' in self.kwargs:
            context['module'] = course.modules.get(id=self.kwargs['module_id'])

        else:
            context['module'] = course.modules.all()[0]
        return context
