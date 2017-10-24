from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.join_mailing_list, name='mailing'),
]
