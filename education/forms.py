from django import forms

from courses.models import Course


class CourseSubscribeForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)
