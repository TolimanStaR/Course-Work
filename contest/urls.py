from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContestList.as_view(), name='contest_list'),
]
