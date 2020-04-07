from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Contest


class ContestList(ListView):
    template_name = 'list.html'
    model = Contest


class ContestDetail(DetailView):
    template_name = 'contest/det.html'
    model = Contest