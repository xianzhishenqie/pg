# -*- coding: utf-8 -*-
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SERVER = 'http://192.168.1.107:8000'


PG_APPS = [
    'base',
    'pg_auth',
    'we',
    'album',
]


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