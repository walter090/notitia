from django.db import models
from django.core import validators
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(_('email'),
                             max_length=200,
                             validators=[validators.EmailValidator],
                             null=False,
                             blank=False,
                             primary_key=True,
                             unique=True)
    password = models.CharField(_('password'),
                                max_length=200,
                                null=False,
                                blank=False)
    first_name = models.CharField(_('first_name'),
                                  max_length=200,
                                  blank=True)
    last_name = models.CharField(_('last name'),
                                 max_length=200,
                                 blank=True)
    member_since = models.DateField(_('date joined'), null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def get_full_name(self):
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        try:
            short = self.first_name[0].upper() + self.last_name[0].upper()
        except IndexError:
            return ''
        return short

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
