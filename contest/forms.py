from django import forms


class ContestRegistrationForm(forms.Form):
    agreed = forms.BooleanField(required=True)


class SolutionSendForm(forms.Form):
    LANG_CHOICES = (
        ('GNU GCC C99', 'GNU GCC C99'),
        ('GNU G++ 17', 'GNU G++ 17'),
        # ('Kotlin', 'Kotlin'),
        ('Python 3', 'Python 3'),
        ('PyPy', 'PyPy'),
        # ('Ruby 2.7', 'Ruby 2.7'),
    )

    language = forms.ChoiceField(choices=LANG_CHOICES, label="Выберите язык")
    participant_file = forms.FileField(label="Загрузить файл")
