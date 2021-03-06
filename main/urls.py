from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('search/<search_text>/', views.ArticleListView.as_view(), name='article_list'),
    path('privacy/', views.Privacy.as_view(), name='privacy'),
]
