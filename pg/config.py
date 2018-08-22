# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SERVER = 'http://www.shixiaobo.com'

RESOURCE_SERVER = ''


PG_APP_PATHS = [
    ('base', ''),
    'pg_auth',
    # ('map', ''),
    'we',
    ('album', ''),
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


APP_SETTINGS = {

}


USE_CDN = True