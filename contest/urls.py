from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContestList.as_view(), name='contest_list'),
    path('<int:pk>/', views.ContestDetail.as_view(), name='contest_detail'),
    path('<int:pk>/register/', views.ContestRegistrationView.as_view(), name='contest_register'),
    path('<int:pk>/problemset/', views.ContestDetail.ContestTaskListView.as_view(), name='contest_task_list'),
    path('<int:pk>/rating/', views.ContestDetail.ContestRatingView.as_view(), name='contest_rating')
]
