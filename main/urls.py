
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.shortcuts import HttpResponse
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path(r'', views.index, name='index'),
]
