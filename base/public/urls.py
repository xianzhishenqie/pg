# -*- coding: utf-8 -*-

from django.conf import settings
from django.urls import re_path
from django.views.static import serve

from . import views


urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), views.media, name='media'),
]

