# -*- coding: utf-8 -*-
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SERVER = 'http://www.shixiaobo.com'


PG_APP_PATHS = [
    ('base', ''),
    'pg_auth',
    'we',
    ('album', ''),
]

PG_APPS = []
PG_APP_PATH = {}
for app_path in PG_APP_PATHS:
    if isinstance(app_path, tuple):
        PG_APPS.append(app_path[0])
        PG_APP_PATH[app_path[0]] = app_path[1]
    else:
        PG_APPS.append(app_path)
        PG_APP_PATH[app_path] = app_path


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'album',
        'USER': 'album',
        'PASSWORD': 'album',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}