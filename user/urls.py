#coding=utf-8
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'login', views.user_login),
    url(r'logout', views.user_logout)
]
