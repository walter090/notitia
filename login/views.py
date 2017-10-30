from django.views.generic import FormView
from django.shortcuts import render


class LoginView(FormView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        raise NotImplementedError


class SignUpView(FormView):
    template_name = 'login/signup.html'

    def get(self, request, *args, **kwargs):
        raise NotImplementedError
