from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


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


@login_required
def profile(request):
    return render(request, 'account/profile.html', {'section': 'profile'})
