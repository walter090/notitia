from django.db import models
from django.core import validators


class Email(models.Model):
    email_address = models.CharField(max_length=100, validators=[validators.EmailValidator])
    joined_date = models.DateTimeField('date joined')
