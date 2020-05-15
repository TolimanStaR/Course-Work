from .base import *

DEBUG = True

# ADMINS = ('Даниил Дыряев', 'toliman.st4r@gmail.com')

# Для запуска на Linux:
# python3.8 manage.py runserver --settings=Coursework.settings.pro

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'olympus',
        'USER': 'olympus',
        'PASSWORD': '528491pisos',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# STATIC_ROOT = '/root/project/main/static/'
# MEDIA_ROOT = '/root/project/media/'
