import os

from importlib import import_module

from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings, LazySettings, Settings
from django.urls import include, path

from base.utils.rest.routers import api_path
from base.utils.thread import async_exe, async_exe_once


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
            urls_module = import_module(urls_name)
            if hasattr(urls_module, 'viewsets'):
                urls_module.urlpatterns += api_path(urls_module.viewsets, app_name)
            patterns.append(
                path(_get_sub_path(path_name), include((urls_name, app_name), namespace=sub_module_name))
            )
    return patterns


def get_pg_urls(collect_app_urls=True):
    patterns = []
    for app_name in settings.PG_APP_NAMES:
        urls_name = '{app_name}.urls'.format(
            app_name=app_name,
        )
        urls_path = os.path.join(settings.BASE_DIR, urls_name.replace('.', '/') + '.py')
        if os.path.exists(urls_path):
            urls_module = import_module(urls_name)
            if collect_app_urls:
                urls_module.urlpatterns += get_app_urls(app_name)
            path_name = settings.PG_APP_PATH[app_name]
            patterns.append(
                path(_get_sub_path(path_name), include((urls_name, app_name), namespace=app_name))
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


def load_app_settings(package):
    app_name = get_app_name(package)
    app_settings = LazyAppSettings(app_name)
    settings.MS[app_name] = app_settings
    return app_settings


def sync_app_settings(app_name):
    app_module = import_module(app_name)
    if hasattr(app_module, 'sync_app_settings'):
        app_module.sync_app_settings()

def sync_init(app_name):
    app_module = import_module(app_name)
    if hasattr(app_module, 'sync_init'):
        app_module.sync_init()
    if hasattr(app_module, 'async_init'):
        async_exe(app_module.async_init)
    if hasattr(app_module, 'async_global_init'):
        async_exe_once(app_module.async_global_init)


class AppConfig(DjangoAppConfig):

    def ready(self):
        sync_init(self.name)


class LazyAppSettings(LazySettings):

    _app_name = None

    def __init__(self, app_name):
        self._app_name = app_name
        super(LazyAppSettings, self).__init__()

    def _setup(self, name=None):
        self._wrapped = AppSettings(self._app_name)

    def __setattr__(self, name, value):
        if name == '_app_name':
            self.__dict__['_app_name'] = value
        else:
            if name == '_wrapped':
                _app_name = self.__dict__.pop('_app_name', None)
                self.__dict__.clear()
                self.__dict__['_app_name'] = _app_name
            else:
                self.__dict__.pop(name, None)
            super(LazySettings, self).__setattr__(name, value)


class AppSettings(Settings):

    def __init__(self, app_name):
        app_settings_module = '{app_name}.setting'.format(
            app_name=app_name,
        )
        default_app_settings = import_module(app_settings_module)
        for setting in dir(default_app_settings):
            if setting.isupper():
                setattr(self, setting, getattr(default_app_settings, setting))

        # store the settings module in case someone later cares
        self.SETTINGS_MODULE = app_settings_module

        self._explicit_settings = set()
        config_settings = settings.APP_SETTINGS.get(app_name)
        if config_settings:
            for setting, setting_value in config_settings.items():
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)

