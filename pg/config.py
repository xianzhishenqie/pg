# -*- coding: utf-8 -*-
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PG_APPS = [
    'base',
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