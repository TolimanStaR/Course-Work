from django import forms
from .models import Comment


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=300)


class CommentForm(forms.Form):
    body = forms.CharField()
