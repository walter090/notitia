from django.db import models
from django.core import validators
from django import forms


class MailingListSubscriber(models.Model):
    email_address = models.CharField(max_length=100,
                                     validators=[validators.EmailValidator],
                                     null=False,
                                     blank=False,
                                     primary_key=True)
    joined_date = models.DateTimeField('date joined')

    def ___str__(self):
        return self.email_address


class MailingListForm(forms.ModelForm):
    class Meta:
        model = MailingListSubscriber
        fields = ['email_address']
