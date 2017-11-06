from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from . import models


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MakePostView(FormView):
    template_name = 'interaction/make_post.html'

    def get(self, request, *args, **kwargs):
        authorized = request.user.is_authenticated()
        full_name = request.user.get_full_name()

        if authorized:
            status = 'You are logged in.'
            name = full_name if not full_name.isspace() else request.user.email
            template_file = 'account_modal.html'
        else:
            status = 'You are not logged in.'
            name = ''
            template_file = 'login_form.html'

        return render(request, self.template_name, context={
            'section_name': 'Draft',
            'logged_in': status,
            'name': name,
            'template_file': template_file,
        })

    def post(self, request, *args, **kwargs):
        raise NotImplementedError
