from .models import User
from django import forms


class SignupForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    confirm_password = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('The passwords don\'t match!')
