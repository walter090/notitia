from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.utils.translation import ugettext_lazy as _

from . import models


@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class MakePostView(FormView):
    template_name = 'interaction/make_post.html'

    def get(self, request, *args, **kwargs):
        full_name = request.user.get_full_name()

        status = 'You are logged in.'
        name = full_name if not full_name.isspace() else request.user.email
        template_file = 'account_modal.html'
        return render(request, self.template_name,
                      context={
                          'section_name': _('Draft'),
                          'logged_in': _(status),
                          'name': name,
                          'template_file': template_file,
                      })

    def post(self, request, *args, **kwargs):
        data = request.POST
        story = models.Post()
        story.make_new_post(request=request,
                            title=data['title'],
                            content_body=data['content_body'])
        story.subtitle = data['subtitle'].strip()
        story.tldr = data['tldr'].strip()
        messages = []
        try:
            story.save()
            messages += 'Your post is published.'
            return JsonResponse({
                'messages': messages,
                'url': '/login/',
                'all_clear': True,
            })
        except ValidationError as ve:
            messages += ve
            return JsonResponse({
                'messages': messages,
                'url': '/new-story/',
                'all_clear': False,
            })
