from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from registro import views

urlpatterns = [
    re_path(r'registro/$', views.RegistroList.as_view()),
    re_path(r'registro/(?P<id>\d+)$', views.RegistroDetail.as_view()),
]