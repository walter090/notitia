from django import forms
from django.core import validators
from notitia import settings


class SignupForm(forms.Form):
    email = forms.EmailField(max_length=200,
                             validators=[validators.EmailValidator])
    password = forms.CharField(max_length=200)
    confirm_password = forms.CharField(max_length=200)
