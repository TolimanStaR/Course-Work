from django.shortcuts import render, get_object_or_404

from django.db.models import Count
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView

from courses.models import Subject, Course


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
