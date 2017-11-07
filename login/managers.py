import datetime

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **kwargs):
        email = self.normalize_email(email)

        user = self.model(email=email,
                          member_since=datetime.date.today(),
                          first_name=first_name.strip(),
                          last_name=last_name.strip(),
                          **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, password, first_name, last_name, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email=email,
                                 password=password,
                                 first_name=first_name,
                                 last_name=last_name, **kwargs)

    def create_superuser(self, email, password, first_name, last_name, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)

        if kwargs.get('is_superuser') is not True or kwargs.get('is_staff') is not True:
            raise ValueError('Superuser cannot be created.')

        return self._create_user(email=email,
                                 password=password,
                                 first_name=first_name,
                                 last_name=last_name, **kwargs)
