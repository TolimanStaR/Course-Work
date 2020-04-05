from django.contrib.postgres.search import TrigramSimilarity, SearchVector, SearchQuery, SearchRank
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from .models import Article, Comment
from .forms import SearchForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def search_queryset(text):
    search_vector = SearchVector('title', weight='A') + \
                    SearchVector('content', weight='B') + \
                    SearchVector('author', weight='C')
    search_query = SearchQuery(text)
    result = Article.objects.annotate(
        rank=SearchRank(search_vector, search_query)
    ).filter(rank__gte=0.3).order_by('-rank')

    return result


def paginate_page(paginator, page):
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    return article_list


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

        paginator = Paginator(article_list, 1)
        page = request.GET.get('page')
        article_list = paginate_page(paginator, page)

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

        paginator = Paginator(article_list, 1)
        page = request.GET.get('page')
        article_list = paginate_page(paginator, page)

        return render(request, self.template_name,
                      {'object_list': article_list, 'form': search_form, 'search_text': search_text})


class ArticleDetailView(DetailView, FormView):
    template_name = 'articles/detail.html'
    model = Article
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        pk = kwargs['pk'] if 'pk' in kwargs else 1
        article = get_object_or_404(Article, pk=pk)
        return render(request, self.template_name, {'article': article, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        pk = kwargs['pk'] if 'pk' in kwargs else 1
        article = get_object_or_404(Article, pk=pk)
        if form.is_valid():
            comment = Comment.objects.create(
                body=form.cleaned_data['body'],
                user=request.user.user_profile,
                article=article
            )
            comment.save()
            return HttpResponseRedirect(request.path)
        else:
            form = self.form_class
        return render(request, self.template_name, {'article': article, 'form': form})
