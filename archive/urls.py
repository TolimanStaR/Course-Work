from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='archive_task_list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='archive_task_detail'),
    path('<int:pk>/packages/', views.ArchivePackageView.as_view(), name='archive_package_list'),
    path('<int:pk>/packages/<int:id>/', views.ArchivePackageView.as_view(), name='archive_package_detail'),
]
