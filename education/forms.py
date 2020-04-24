from django import forms

from courses.models import Course

from contest.forms import SolutionSendForm


class CourseSubscribeForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)


class CourseSolutionSendForm(SolutionSendForm):
    pass
