import json

from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from . import models, forms


class LoginView(FormView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        login_email = request.POST['email']
        login_password = request.POST['password']
        user = authenticate(request,
                            email=login_email,
                            password=login_password)
        if user is not None:
            login(request, user=user)
            return HttpResponseRedirect('/welcome/')
        else:
            return render(request, self.template_name,
                          context={
                              'submitted': 'User with this email address does not exist.',
                          })


class SignupView(FormView):
    template_name = 'login/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        signup_form = forms.SignupForm(request.POST)

        if signup_form.is_valid():
            data = signup_form.cleaned_data
            user = models.User.objects.create_user(email=data['email'],
                                                   password=data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()

            return render(request, LoginView.template_name,
                          context={
                              'registered': 'Welcome!'
                          })

        errors_dict = json.loads(signup_form.errors.as_json())
        error_message = ''
        print(errors_dict)

        for error_type in errors_dict:
            for error in errors_dict[error_type]:
                error_message += error['message']

        return render(request, self.template_name,
                      context={
                          'submitted': error_message,
                      })
