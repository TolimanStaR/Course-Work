from functools import update_wrapper

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, DetailView, ListView

from .forms import LoginForm, UserRegistrationForm, UserEditForm, UserProfileEditForm
from .models import UserProfile, User


class UserRegistration(FormView):
    template_name = 'account/register.html'
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user=new_user, profile_image='images/default_avatar.png')
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            messages.error(request, 'Пользователь с таким ником уже зарегистрирован. Пожалуйста, выберите другой ник.')
            user_form = self.form_class
            return render(request, 'account/register.html', {'user_form': user_form})

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


class UserListView(ListView):
    template_name = 'account/users.html'
    model = User


class UserProfileView(DetailView, LoginRequiredMixin):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        if 'username' in kwargs:
            user = get_object_or_404(User, username=kwargs['username'])
        else:
            user = User.objects.get(username=request.user.username)

        return render(request, self.template_name, {'user': user})

# TODO: Заменить login view на свой класс
