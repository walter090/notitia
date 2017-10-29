from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.JoinListView.as_view(), name='mailing'),
]
