from django.db import models
from django.core import validators
from notitia import settings


class User(models.Model):
    email = models.CharField(max_length=100,
                             validators=[validators.EmailValidator],
                             primary_key=True)
    password = models.CharField(max_length=100,
                                validators=settings.AUTH_PASSWORD_VALIDATORS)

    def __str__(self):
        return self.email
