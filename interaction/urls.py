from django.urls import path
from . import views

urlpatterns = [
    path('', views.MakePostView.as_view(), name='make_post'),
]
