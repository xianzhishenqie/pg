# -*- coding: utf-8 -*-
import os

from importlib import import_module

from django.conf import settings
from django.urls import include, path, re_path



def get_app_name(module_name):
    return module_name.split('.')[0]


def get_service_name(module_name):
    return module_name.split('.')[1]


def get_app_service_name(module_name):
    return module_name.split('.')[0:2]


def _get_sub_path(path_name):
    if path_name:
        return '{path_name}/'.format(path_name=path_name)
    else:
        return path_name


def get_app_urls(app_name):
    patterns = []
    for sub_module_name, path_name in settings.SUB_MODULES:
        urls_name = '{app_name}.{sub_module}.urls'.format(
            app_name=app_name,
            sub_module=sub_module_name,
        )
        urls_path = os.path.join(settings.BASE_DIR, urls_name.replace('.', '/') + '.py')
        if os.path.exists(urls_path):
            import_module(urls_name)
            patterns.append(
                path(_get_sub_path(path_name), include((urls_name, app_name), namespace=sub_module_name))
            )
    return patterns


def get_pg_urls(collect_app_urls=True):
    patterns = []
    for app_name in settings.PG_APPS:
        urls_name = '{app_name}.urls'.format(
            app_name=app_name,
        )
        urls_path = os.path.join(settings.BASE_DIR, urls_name.replace('.', '/') + '.py')
        if os.path.exists(urls_path):
            urls_module = import_module(urls_name)
            if collect_app_urls:
                urls_module.urlpatterns += get_app_urls(app_name)
            patterns.append(
                path(_get_sub_path(app_name), include((urls_name, app_name), namespace=app_name))
            )
        else:
            if collect_app_urls:
                app_urlpatterns = get_app_urls(app_name)
                if app_urlpatterns:
                    path_name = settings.PG_APP_PATH[app_name]
                    patterns.append(
                        path(_get_sub_path(path_name), include((app_urlpatterns, app_name), namespace=app_name))
                    )

    return patterns