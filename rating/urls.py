from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.UserRatingListView.as_view(),
         name='user_rating_list')
]
