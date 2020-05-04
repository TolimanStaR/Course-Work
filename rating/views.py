from django.shortcuts import render
from django.views.generic import ListView


from account.models import UserProfile


class UserRatingListView(ListView):
    template_name = 'user_rating.html'
    model = UserProfile
    paginate_by = 50

