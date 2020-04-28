from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import TemplateResponseMixin, View

from .models import Contest
from .forms import ContestRegistrationForm, SolutionSendForm

from account.models import UserProfile
from contest.models import ContestParticipant, Contest, ContestTask, ContestSolutionCase, ContestTest
from management.task_manager import *
from management.complete_contest import complete_contest

from django.core.exceptions import ObjectDoesNotExist

import multiprocessing
import time
import datetime
import pytz
import os


class ContestList(ListView):
    template_name = 'list.html'
    model = Contest


def contest_list(request, pk=None):
    if pk:
        contest = get_object_or_404(Contest, pk=pk)
        cur_time = datetime.datetime.now(datetime.timezone.utc)

        if cur_time < contest.starts_at:
            contest.active = False
            contest.completed = False
            contest.save()
            return HttpResponseRedirect(reverse('contest_waiting', args=(pk,)))

        if contest.starts_at <= cur_time <= contest.starts_at + datetime.timedelta(minutes=contest.duration_minutes):

            if not contest.active:
                contest.active = True

            if contest.completed:
                contest.completed = False
                
            contest.save()

            return render(request, 'contest/task_list.html', {'contest': contest})

        if cur_time > contest.starts_at + datetime.timedelta(minutes=contest.duration_minutes):

            if not contest.completed:
                contest.completed = True
                contest.save()
                complete_contest(contest.pk)

            return HttpResponseRedirect(reverse('contest_result', args=(pk,)))

    else:
        return HttpResponseRedirect(reverse('contest_list'))


class ContestWaiting(LoginRequiredMixin, DetailView):
    template_name = 'contest/waiting.html'
    model = Contest

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            contest = get_object_or_404(Contest, pk=kwargs['pk'])
            cur_time = datetime.datetime.now(datetime.timezone.utc)

            if cur_time < contest.starts_at:
                contest.active = False
                contest.completed = False
                contest.save()
                return render(request, 'contest/waiting.html', {'contest': contest})

            elif contest.starts_at <= cur_time <= contest.starts_at + datetime.timedelta(
                    minutes=contest.duration_minutes):
                return HttpResponseRedirect(reverse('contest_task_list', args=(kwargs['pk'],)))

            else:
                if not contest.completed:
                    contest.completed = True
                    contest.save()
                    complete_contest(contest.pk)

                return HttpResponseRedirect(reverse('contest_result', args=(kwargs['pk'],)))


class ContestDetail(LoginRequiredMixin, DetailView):
    template_name = 'contest/detail.html'
    model = Contest

    class ContestTaskListView(DetailView):
        template_name = 'contest/task_list.html'
        model = Contest

    class ContestRatingView(DetailView):
        template_name = 'contest/rating.html'
        model = Contest

    class ContestPackageView(DetailView):
        template_name = 'contest/packages.html'
        model = Contest

    class ContestTaskDetailView(LoginRequiredMixin, DetailView, FormView):
        template_name = 'contest/task_detail.html'
        model = Contest

        def get(self, request, *args, **kwargs):
            if 'pk' in kwargs and 'difficulty' in kwargs:
                contest = Contest.objects.get(pk=kwargs['pk'])

                if not contest.active:
                    return HttpResponseRedirect(reverse('contest_waiting', args=(kwargs['pk'],)))

                task = get_object_or_404(ContestTask, contest=contest, difficulty=kwargs['difficulty'])
                task_tests = ContestTest.objects.filter(task=task)
                first_test = task_tests[0]

                form = SolutionSendForm

                return render(request, self.template_name,
                              {'contest': contest,
                               'task': task,
                               'first_test': first_test,
                               'form': form})

        def post(self, request, *args, **kwargs):
            contest = Contest.objects.get(pk=kwargs['pk'])
            task = get_object_or_404(ContestTask, contest=contest, difficulty=kwargs['difficulty'])
            task_tests = ContestTest.objects.filter(task=task)
            participant = ContestParticipant.objects.get(contest=contest, user=request.user.user_profile)
            form = SolutionSendForm(request.POST, request.FILES)

            if form.is_valid():
                participant_file = form.cleaned_data['participant_file']
                lang = form.cleaned_data['language']
                code = participant_file.open('r').read().decode('cp866')
                cur_time = datetime.datetime.now(datetime.timezone.utc)

                package = ContestSolutionCase.objects.create(
                    participant=participant,
                    task=task,
                    task_file=participant_file,
                    language=lang,
                    task_code=code,
                )

                package.verdict = check_participant_solution(package, task, task_tests)

                if package.verdict == verdict[True]:
                    package.solved = True
                    if participant.stats[task.number - 1] != 1:
                        participant.stats[task.number - 1] = 1
                        participant.task_solved += 1
                        task.solved_by += 1
                else:
                    if participant.stats[task.number - 1] != 1:
                        participant.stats[task.number - 1] = -1

                participant.penalty += int((cur_time - contest.starts_at).total_seconds() // 60)

                participant.save()
                package.save()
                task.save()

                return HttpResponseRedirect(reverse('contest_packages_list', args=(contest.pk, task.difficulty)))

            return HttpResponse('Please try again')

    class ContestPackageListView(LoginRequiredMixin, TemplateResponseMixin, View):
        model = Contest
        template_name = 'contest/packages_list.html'

        def get(self, request, pk=None, difficulty=None, id=None):
            if pk and difficulty:
                contest = get_object_or_404(Contest, pk=pk)
                task = get_object_or_404(ContestTask, difficulty=difficulty)
                participant = get_object_or_404(ContestParticipant, user=request.user.user_profile)
                packages = ContestSolutionCase.objects.filter(task=task, participant=participant)

                if id:
                    package = get_object_or_404(ContestSolutionCase, id=id)
                    if request.user.user_profile == package.participant.user:
                        return render(request, 'contest/packages_detail.html', {
                            'contest': contest,
                            'task': task,
                            'participant': participant,
                            'package': package,
                        })
                    else:
                        return HttpResponseRedirect(reverse('contest_task_detail', args=(contest.pk, task.difficulty,)))
                else:
                    return render(request, self.template_name, {
                        'contest': contest,
                        'task': task,
                        'participant': participant,
                        'packages': packages,
                    })


class ContestPackagesDetailView(LoginRequiredMixin):
    pass


class ContestRegistrationView(LoginRequiredMixin, FormView):
    template_name = 'contest/contest_register.html'
    form_class = ContestRegistrationForm

    def get(self, request, *args, **kwargs):
        errors = None
        form = self.form_class

        if 'pk' in kwargs:
            contest = get_object_or_404(Contest, pk=kwargs['pk'])
            user_profile = get_object_or_404(UserProfile, user=request.user)
        else:
            errors = True
            messages.error(request, 'Возникла ошибка, попробуйте снова')
            contest, user_profile = None, None

        return render(request, self.template_name,
                      {'user_profile': user_profile, 'contest': contest, 'form': form, 'errors': errors})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        user_profile = UserProfile.objects.get(user=request.user)
        contest = Contest.objects.get(pk=kwargs['pk'])

        if form.is_valid():
            try:
                ContestParticipant.objects.get(user=user_profile, contest=contest)
                message = f'Вы уже регистрировались на соревнование {contest.title} под этим ником'
            except ObjectDoesNotExist:
                ContestParticipant.objects.create(
                    user=user_profile,
                    contest=contest,
                    stats=[0] * 16
                )
                contest.participants_count += 1
                contest.save()
                message = f'Вы успешно зарегистрировались на соревнование {contest.title} ' \
                          f'под ником {user_profile.user.username}'

            return HttpResponseRedirect(reverse('contest_waiting', args=(contest.pk,)))
        else:
            messages.error(request, 'Необходимо согласиться с правилами!')
            return render(request, self.template_name,
                          {'user_profile': user_profile, 'contest': contest, 'form': form})


class ContestResultView(TemplateResponseMixin, View):
    template_name = 'contest/contest_result.html'
    model = Contest

    def get(self, request, pk=None):
        contest = get_object_or_404(Contest, pk=pk)
        return render(request, self.template_name, {'contest': contest})
