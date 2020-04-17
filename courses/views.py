from django.urls import reverse_lazy
from django.forms.models import modelform_factory
from django.apps import apps
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView

from braces.views import GroupRequiredMixin

from .models import Course, Module, Content
from .forms import ModuleFormSet


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
    group_required = u'Instructor'


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


class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user.user_profile)
        return super(CourseModuleUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({'course': self.course, 'formset': formset})


class ContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'courses/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in [
            'text',
            'video',
            'image',
            'file',
            'code',
            'task',
        ]:
            return apps.get_model(app_label='courses', model_name=model_name)

        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner', 'order', 'created', 'updated'])
        return Form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        self.module = get_object_or_404(Module,
                                        id=module_id,
                                        course__owner=request.user.user_profile)
        self.model = self.get_model(model_name)

        if id:
            self.obj = get_object_or_404(self.model,
                                         id=id,
                                         owner=request.user.user_profile)

        return super(ContentCreateUpdateView, self).dispatch(request, module_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj, data=request.POST, files=request.FILES)
        return self.render_to_response({'form': form, 'object': self.obj})

    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj, data=request.POST, files=request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user.user_profile
            obj.save()

            if not id:
                Content.objects.create(module=self.module, item=obj)

            return redirect('module_content_list', self.module.id)
        return self.render_to_response({'form': form, 'object': self.obj})
