import json

from django.views.generic import FormView, View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext as _

from . import models, forms


class LoginView(FormView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      context={
                          'section_name': _('Sign in')
                      })

    def post(self, request, *args, **kwargs):
        login_email = request.POST['email']
        login_password = request.POST['password']
        user = authenticate(request,
                            email=login_email,
                            password=login_password)
        if user is not None:
            login(request, user=user)
            return redirect(request.GET.get('next', ''))
        else:
            return render(request, self.template_name,
                          context={
                              'submitted': _('Email or password is not correct.'),
                          })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class SignupView(FormView):
    template_name = 'login/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      context={
                          'section_name': _('Register'),
                      })

    def post(self, request, *args, **kwargs):
        signup_form = forms.SignupForm(request.POST)

        if signup_form.is_valid():
            data = signup_form.cleaned_data
            models.User.objects.create_user(email=data['email'],
                                            password=data['password'],
                                            first_name=data['first_name'],
                                            last_name=data['last_name'])
            # user.save()
            return render(request, LoginView.template_name,
                          context={
                              'registered': _('Welcome!'),
                          })

        errors_dict = json.loads(signup_form.errors.as_json())
        error_message = ''
        print(errors_dict)

        for error_type in errors_dict:
            for error in errors_dict[error_type]:
                error_message += error['message']

        return render(request, self.template_name,
                      context={
                          'submitted': _(error_message),
                      })


class AccountView(FormView):
    template_name = 'login/account.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      context={
                          'section_name': _('Account'),
                          'modal_template': 'account_modal.html',
                      })

    def post(self, request, *args, **kwargs):
        raise NotImplementedError


# class MasterView(object):
#     """
#     This view should handle core tasks of all views.
#     """
#     # TODO Implement a master view that all views inherit from.
#     raise NotImplementedError
