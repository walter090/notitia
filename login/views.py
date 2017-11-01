import datetime
import json

from django.views.generic import FormView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models, forms
from django.contrib.auth import hashers


class LoginView(FormView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        raise NotImplementedError


class SignupView(FormView):
    template_name = 'login/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        signup_form = forms.SignupForm(request.POST)

        if signup_form.is_valid():
            data = signup_form.cleaned_data
            user = models.User()
            user.email = data['email']
            user.password = hashers.make_password(data['password'])
            user.member_since = datetime.date.today()
            user.save()

            return HttpResponseRedirect('/login/')

        errors_dict = json.loads(signup_form.errors.as_json())
        error_message = ''
        print(errors_dict)

        for error_type in errors_dict:
            for error in errors_dict[error_type]:
                error_message += error['message']

        return render(request, self.template_name, context={
            'submitted': error_message,
        })
