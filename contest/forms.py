from django import forms


class ContestRegistrationForm(forms.Form):
    agreed = forms.BooleanField(required=True)


class SolutionSendForm(forms.Form):
    LANG_CHOICES = (
        ('GNU GCC', 'GNU GCC'),
        ('GNU G++', 'GNU G++'),
        ('Kotlin', 'Kotlin'),
        ('Python 3', 'Python 3'),
        ('Ruby 2.7', 'Ruby 2.7'),
    )

    language = forms.ChoiceField(choices=LANG_CHOICES)
    participant_file = forms.FileField()
