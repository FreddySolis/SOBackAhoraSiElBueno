from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from carrera import views

urlpatterns = [
    re_path(r'carreras/$', views.CarreraList.as_view()),
    re_path(r'carreras/(?P<id>\d+)$', views.CarreraDetail.as_view()),
]