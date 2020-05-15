# Using standart django authentication handlers:

from django.contrib.auth import views as authentication_views

from Coursework.settings.base import LOGOUT_REDIRECT_URL

# ...

from django.urls import path
from . import views

urlpatterns = [
    path('', authentication_views.LoginView.as_view(), name='login'),
    path('login/', authentication_views.LoginView.as_view(), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(), {'next_page': LOGOUT_REDIRECT_URL}, name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/<username>/', views.UserProfileView.as_view(), name='profile'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('change-password/', authentication_views.PasswordChangeView.as_view(), name='change_password'),
    path('change-password/done/', authentication_views.PasswordChangeDoneView.as_view(), name='change_password_done'),
    path('reset-password/', authentication_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', authentication_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authentication_views.PasswordResetConfirmView.as_view(),
         name='reset_password_confirm'),
    path('reset/done/', authentication_views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('edit-profile/', views.UserEditProfile.as_view(), name='edit'),
    path('profile/<username>/packages/', views.UserPackageView.as_view(), name='profile_packages'),
]
