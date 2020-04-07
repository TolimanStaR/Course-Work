from django.shortcuts import render
from django.views.generic import ListView
from .models import Contest


class ContestList(ListView):
    template_name = 'list.html'
    model = Contest
