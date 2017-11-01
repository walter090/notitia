from django.db import models
from django.core import validators
from notitia import settings
from django.contrib.auth import hashers


class User(models.Model):
    email = models.CharField(max_length=200,
                             validators=[validators.EmailValidator(message='Please enter a valid email address')],
                             null=False,
                             primary_key=True)
    password = models.CharField(max_length=200,
                                null=False)
    member_since = models.DateField('date joined', null=True)

    def __str__(self):
        return self.email
