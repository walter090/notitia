from django.db import models
from django.core import validators


class User(models.Model):
    email = models.CharField(max_length=200,
                             validators=[validators.EmailValidator],
                             null=False,
                             blank=False,
                             primary_key=True,
                             unique=True)
    password = models.CharField(max_length=200,
                                null=False,
                                blank=False)
    member_since = models.DateField('date joined', null=True)

    def __str__(self):
        return self.email
