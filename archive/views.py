from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.base import TemplateResponseMixin, View

from .models import ArchiveTask, ArchiveTest, ArchiveSolutionCase
from .forms import PackageSendForm
from account.models import UserProfile

from management.task_manager import verdict, check_participant_solution


class TaskListView(ListView):
    template_name = 'archive_list.html'
    model = ArchiveTask
    paginate_by = 3


class TaskDetailView(LoginRequiredMixin, FormView):
    template_name = 'archive_detail.html'
    form_class = PackageSendForm

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(ArchiveTask, pk=kwargs['pk'])
        form = self.form_class
        first_test = ArchiveTest.objects.filter(task=task)[0]

        return render(request, self.template_name, {'task': task, 'form': form, 'first_test': first_test})

    def post(self, request, *args, **kwargs):
        form = PackageSendForm(request.POST, request.FILES)
        if form.is_valid():
            task = ArchiveTask.objects.get(pk=kwargs['pk'])
            user = UserProfile.objects.get(user=request.user)
            tests = ArchiveTest.objects.filter(task=task)

            user_file = form.cleaned_data['participant_file']
            language = form.cleaned_data['language']

            code = user_file.open('r').read().decode('cp866')

            package = ArchiveSolutionCase.objects.create(
                user=user,
                task=task,
                task_file=user_file,
                language=language,
                task_code=code,
            )

            package.verdict = check_participant_solution(
                package=package,
                task=task,
                tests=tests
            )

            try:
                right_packages = ArchiveSolutionCase.objects.filter(task=task, user=user, solved=True)
            except ObjectDoesNotExist:
                task.solved_by += 1

            if package.verdict == verdict[True]:
                package.solved = True

            package.save()

            return HttpResponseRedirect(reverse('archive_package_list', args=(task.pk,)))

        else:
            return HttpResponseRedirect(reverse('archive_task_list', args=()))


class ArchivePackageView(LoginRequiredMixin, TemplateResponseMixin, View):
    model = ArchiveTask
    template_name = 'packages/archive_package_list.html'

    def get(self, request, pk=None, id=None):
        if pk:
            task = get_object_or_404(ArchiveTask, pk=pk)
            packages = ArchiveSolutionCase.objects.filter(task=task, user=request.user.user_profile)

            if id:
                package = get_object_or_404(ArchiveSolutionCase, id=id)
                return render(request, 'packages/archive_package_detail.html', {'task': task, 'package': package})
            else:
                return render(request, self.template_name, {'task': task, 'packages': packages})
