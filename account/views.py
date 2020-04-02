from functools import update_wrapper

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView

from .forms import LoginForm, UserRegistrationForm, UserEditForm, UserProfileEditForm
from .models import UserProfile


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        user = None

        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(
                request,
                username=clean_data['username'],
                password=clean_data['password'],
            )

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Вы вошли в аккаунт')
            else:
                return HttpResponse('Аккаунт не активен')
        else:
            return HttpResponse('Некорректный логин или пароль!')
    else:
        form = LoginForm

    return render(
        request,
        'account/login.html',
        {'form': form}
    )


class UserRegistration(FormView):
    template_name = 'account/register.html'
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})

    def get(self, request, *args, **kwargs):
        user_form = self.form_class
        return render(request, 'account/register.html', {'user_form': user_form})


class UserEditProfile(FormView, LoginRequiredMixin):
    template_name = 'account/edit_profile.html'

    def post(self, request, *args, **kwargs):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        user_profile_form = UserProfileEditForm(
            instance=request.user.user_profile,
            data=request.POST,
            files=request.FILES,
        )

        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            messages.success(request, 'Профиль успешно обновлен')

            return render(
                request,
                'account/edit_profile.html',
                {'user_form': user_form, 'user_profile_form': user_profile_form}
            )

        else:
            messages.error(request, 'Возникла ошибка при обновлении профиля')

    def get(self, request, *args, **kwargs):
        user_form = UserEditForm(instance=request.user)
        user_profile_form = UserProfileEditForm(instance=request.user.user_profile)
        return render(
            request,
            'account/edit_profile.html',
            {'user_form': user_form, 'user_profile_form': user_profile_form}
        )


@login_required
def profile(request):
    return render(request, 'account/profile.html', {'section': 'profile'})

# TODO: Заменить login_user на свой класс
