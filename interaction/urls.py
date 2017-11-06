from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MakePostView.as_view(), name='make_post'),
]
