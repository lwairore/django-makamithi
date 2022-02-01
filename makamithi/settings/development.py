# This file will contain settings you’ll normally use during development.
from .base import *

DEBUG = True

ALLOWED_HOSTS = config(
    'DEVELOPMENT_ALLOWED_HOSTS',
    cast=lambda v: [s.strip().replace('\'', '') for s in v.split(',')])


DATABASES = {
    'default': {
        'ENGINE': config('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': config('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': config('SQL_USER', 'user'),
        'PASSWORD': config('SQL_PASSWORD', 'password'),
        # 'HOST': config('SQL_HOST', 'localhost'),
        # 'PORT': config('SQL_PORT', '5432'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, '/static')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'staticfiles')
# ]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ORIGIN_WHITELIST = config(
    'DEVELOPMENT_CORS_ORIGIN_WHITELIST',
    cast=lambda v: tuple([s.strip().replace('\'', '') for s in v.split(',')]))
