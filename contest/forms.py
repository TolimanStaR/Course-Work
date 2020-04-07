from django import forms


class ContestRegistrationForm(forms.Form):
    agreed = forms.BooleanField(required=True)
