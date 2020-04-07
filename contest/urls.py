from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContestList.as_view(), name='contest_list'),
    path('<int:pk>/', views.ContestDetail.as_view(), name='contest_detail'),
]
