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
         views.UserSubscribeCourseView,
         name='user_subscribe_course')
]
