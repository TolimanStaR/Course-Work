from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.CourseListView.as_view(),
         name='course_list'),

    path('subject/<slug:subject>/',
         views.CourseListView.as_view(),
         name='course_list_subject'),

    path('course/<slug:slug>/',
         views.CourseDetailView.as_view(),
         name='course_detail'),

    path('subscribe/',
         views.UserSubscribeCourseView.as_view(),
         name='user_subscribe_course'),

    path('courses/',
         views.UserCourseListView.as_view(),
         name='user_course_list'),

    path('course/<int:pk>/',
         views.UserCourseDetailView.as_view(),
         name='user_course_detail'),

    path('course/<int:pk>/<int:module_id>/',
         views.UserCourseDetailView.as_view(),
         name='user_course_detail_module'),

    path('course_check_solution/',
         views.UserCourseCheckTaskView.as_view(),
         name='user_course_detail_module_task_check'),
]
