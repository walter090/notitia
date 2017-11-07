from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^$', views.AccountView.as_view(), name='account'),
]
