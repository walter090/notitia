import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import FormView

from . import models


class JoinListView(FormView):
    template_name = 'mailing/index.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

    def post(self, request, **kwargs):
        sub = models.MailingListSubscriber()
        sub.email_address = request.POST['email']
        sub.joined_date = datetime.datetime.now()
        sub.save()
        return JsonResponse({
            'status': 'Success',
            'message': 'Save successful'
        })
