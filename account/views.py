from functools import update_wrapper

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView

from .forms import LoginForm, UserRegistrationForm


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
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})

    def get(self, request, *args, **kwargs):
        user_form = UserRegistrationForm
        return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def profile(request):
    return render(request, 'account/profile.html', {'section': 'profile'})


# TODO: Заменить login_user на свой класс
