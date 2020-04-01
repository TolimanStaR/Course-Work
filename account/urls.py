# Using standart django authentication handlers:

from django.contrib.auth import views as authentication_views

# ...

from django.urls import path
from . import views

urlpatterns = [
    path('login/', authentication_views.LoginView.as_view(), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
