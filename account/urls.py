# Using standart django authentication handlers:

from django.contrib.auth import views as authentication_views

# ...

from django.urls import path
from . import views

urlpatterns = [
    path('login/', authentication_views.LoginView.as_view(), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', authentication_views.PasswordChangeView.as_view(), name='change_password'),
    path('change-password/done/', authentication_views.PasswordChangeDoneView.as_view(), name='change_password_done'),
    path('reset-password/', authentication_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', authentication_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authentication_views.PasswordResetConfirmView.as_view(),
         name='reset_password_confirm'),
    path('reset/done/', authentication_views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
]
