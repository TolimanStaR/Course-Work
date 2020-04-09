from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContestList.as_view(), name='contest_list'),
    path('<int:pk>/', views.ContestDetail.as_view(), name='contest_detail'),
    path('<int:pk>/register/', views.ContestRegistrationView.as_view(), name='contest_register'),
    path('<int:pk>/problem/<difficulty>/', views.ContestDetail.ContestTaskDetailView.as_view(),
         name='contest_task_detail'),
    path('<int:pk>/problemset/', views.ContestDetail.ContestTaskListView.as_view(), name='contest_task_list'),
    path('<int:pk>/rating/', views.ContestDetail.ContestRatingView.as_view(), name='contest_rating'),
    path('<int:pk>/packages/', views.ContestDetail.ContestPackageView.as_view(), name='contest_packages'),
    path('<int:pk>/problem/<difficulty>/packages/', views.ContestDetail.ContestPackageListView.as_view(),
         name='contest_packages_list'),
    path('<int:pk>/problem/<difficulty>/packages/<int:id>/', views.ContestDetail.ContestPackageListView.as_view(),
         name='contest_package_detail'),
]
