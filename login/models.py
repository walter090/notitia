from django.db import models
from django.core import validators
from notitia import settings
from django.contrib.auth import hashers


class User(models.Model):
    email = models.CharField(max_length=100,
                             validators=[validators.EmailValidator],
                             null=False,
                             primary_key=True)
    password = models.CharField(max_length=100,
                                null=False,
                                validators=[settings.AUTH_PASSWORD_VALIDATORS])
    member_since = models.DateField('date joined', null=True)

    def __str__(self):
        return self.email
