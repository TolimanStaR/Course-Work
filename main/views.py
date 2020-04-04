from django.contrib.postgres.search import TrigramSimilarity, SearchVector, SearchQuery, SearchRank
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from .models import Article, Comment
from .forms import SearchForm


def search_queryset(text):
    search_vector = SearchVector('title', weight='A') + \
                    SearchVector('content', weight='B') + \
                    SearchVector('author', weight='C')
    search_query = SearchQuery(text)
    result = Article.objects.annotate(
        rank=SearchRank(search_vector, search_query)
    ).filter(rank__gte=0.3).order_by('-rank')

    return result


class ArticleListView(ListView, FormView):
    template_name = 'articles/list.html'
    Model = Article

    def get(self, request, *args, **kwargs):

        if 'search_text' in kwargs or 'search_text' in request.GET:
            search_form = SearchForm(initial=request.GET)
            search_text = kwargs['search_text']
            article_list = search_queryset(search_text)
        else:
            article_list = Article.objects.all()
            search_form = SearchForm
            search_text = None

        return render(request, self.template_name,
                      {'object_list': article_list, 'form': search_form, 'search_text': search_text})

    def post(self, request, *args, **kwargs):

        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_text = search_form.cleaned_data['search_text']
            article_list = search_queryset(search_text)
        else:
            article_list = Article.objects.all()
            search_text = None

        return render(request, self.template_name,
                      {'object_list': article_list, 'form': search_form, 'search_text': search_text})


class ArticleDetailView(DetailView):
    template_name = 'articles/detail.html'
    model = Article
