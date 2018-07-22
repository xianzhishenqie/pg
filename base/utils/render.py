# -*- coding: utf-8 -*-
from django.shortcuts import render

from base.utils.app import get_app_service_name


class AppRender(object):

    def __init__(self, module):
        app_name, service_name = get_app_service_name(module)
        self.app_name = app_name
        self.service_name = service_name

    def render(self, request, template_name, context=None, content_type=None, status=None, using=None):
        template_name = '{app_name}/{service_name}/{template_name}'.format(
            app_name=self.app_name,
            service_name=self.service_name,
            template_name=template_name,
        )
        return render(request, template_name, context, content_type, status, using)


def get_app_render(module):
    return AppRender(module).render