from django import forms


class ContestRegistrationForm(forms.Form):
    agreed = forms.BooleanField(required=True)


class SolutionSendForm(forms.Form):
    LANG_CHOICES = (
        ('c', 'GNU C'),
        ('c++', 'GNU C++'),
        ('kt', 'Kotlin'),
        ('py', 'Python 3'),
        ('rb', 'Ruby 2.7'),
    )

    language = forms.ChoiceField(choices=LANG_CHOICES)
    participant_file = forms.FileField()
