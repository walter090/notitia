import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from . import models


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MakePostView(FormView):
    template_name = 'interaction/make_post.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
            'section_name': 'Draft',
        })

    def post(self, request, *args, **kwargs):
        raise NotImplementedError
