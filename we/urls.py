# -*- coding: utf-8 -*-

from django.urls import path

from . import views


urlpatterns = [
    path('code/', views.we_code, name='code'),
]

