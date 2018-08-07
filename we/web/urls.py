# -*- coding: utf-8 -*-

from django.urls import path

from . import views


urlpatterns = [
    path('access/', views.we_access, name='access'),
    # path('code/', views.we_code, name='code'),
]

