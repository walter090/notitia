from django import forms
from django.core import validators
from .models import User


class SignupForm(forms.ModelForm):
    email = forms.EmailField(max_length=200,
                             validators=[validators.EmailValidator],
                             error_messages={
                                 'invalid': 'Please enter a valid email address.\n',
                                 'unique': 'User with this email already exists.\n',
                             })
    password = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('email', 'password')

    # def clean(self):
    #     # Call super clean
    #     super(SignupForm, self).clean()
    #
    #     user_email = self.cleaned_data['email']
    #     try:
    #         User.objects.get(email=user_email)
    #         raise forms.ValidationError('{} is already registered'.format(user_email))
    #     except User.DoesNotExist:
    #         pass
