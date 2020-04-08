from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from .models import Contest
from .forms import ContestRegistrationForm, SolutionSendForm

from account.models import UserProfile
from contest.models import ContestParticipant, Contest, ContestTask, ContestSolutionCase

from django.core.exceptions import ObjectDoesNotExist


class ContestList(ListView):
    template_name = 'list.html'
    model = Contest


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

    class ContestTaskDetailView(DetailView, FormView):
        template_name = 'contest/task_detail.html'

        def get(self, request, *args, **kwargs):
            if 'pk' in kwargs:
                contest = Contest.objects.get(pk=kwargs['pk'])
                task = ContestTask.objects.get(contest=contest, difficulty=kwargs['difficulty'])
                participant = ContestParticipant.objects.get(contest=contest, user=request.user.user_profile)
                form = SolutionSendForm

                return render(request, self.template_name,
                              {'contest': contest, 'task': task, 'participant': participant, 'form': form})

            return HttpResponse('Hello')
            # else:
            #     return HttpResponseRedirect(reverse('contest_detail', args=(1, )))

        def post(self, request, *args, **kwargs):
            return HttpResponse('Hello')


class ContestPackagesListView(LoginRequiredMixin):
    pass


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
                ContestParticipant.objects.get(user=user_profile, contest=contest, stats=[None] * 16)
                message = f'Вы уже регистрировались на соревнование {contest.title} под этим ником'
            except ObjectDoesNotExist:
                ContestParticipant.objects.create(
                    user=user_profile,
                    contest=contest,
                    stats=[None] * 16
                )
                message = f'Вы успешно зарегистрировались на соревнование {contest.title} под ником {user_profile.user.username}'

            return render(request, 'contest/contest_register_done.html',
                          {'user_profile': user_profile, 'message': message})
        else:
            messages.error(request, 'Необходимо согласиться с правилами!')
            return render(request, self.template_name,
                          {'user_profile': user_profile, 'contest': contest, 'form': form})
