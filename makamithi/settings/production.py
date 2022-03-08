# This file will contain settings for use on a production server.
# The production configuration will use settings that will not work in a development environment; for example, forcing the use of HTTPS, adding headers, and using a production database.
# Rerence https://www.digitalocean.com/community/tutorials/how-to-harden-your-production-django-project

from .base import *
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = config(
    'PRODUCTION_ALLOWED_HOSTS',
    cast=lambda v: [s.strip().replace('\'', '') for s in v.split(',')])

MIDDLEWARE.insert(0,  'whitenoise.middleware.WhiteNoiseMiddleware')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ORIGIN_WHITELIST = config(
    'PRODUCTION_CORS_ORIGIN_WHITELIST',
    cast=lambda v: tuple([s.strip().replace('\'', '') for s in v.split(',')]))

# SECURE_SSL_REDIRECT redirects all HTTP requests to HTTPS (unless exempt).
# This means your project will always try to use an encrypted connection.
# You will need to have SSL configured on your server for this to work.
# Note that if you have Nginx or Apache configured to do this already, this setting will be redundant.
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE tells the browser that cookies can only be handled over HTTPS.
# This means cookies your project produces for activities, such as logins, will only work over an encrypted connection.

CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE is the same as SESSION_COOKIE_SECURE but applies to your CSRF token.
# CSRF tokens protect against Cross-Site Request Forgery.
# Django CSRF protection does this by ensuring any forms submitted (for logins, signups, and so on) to your project were created by your project and not a third party.

SECURE_BROWSER_XSS_FILTER = True
# SECURE_BROWSER_XSS_FILTER sets the X-XSS-Protection: 1; mode=block header on all responses that do not already have it.
# This ensures third parties cannot inject scripts into your project.
# For example, if a user stores a script in your database using a public field, when that script is retrieved and displayed to other users it will not run.

X_FRAME_OPTIONS = 'DENY'
# The default is 'SAMEORIGIN', but unless there is a good reason for your site to serve other parts of itself in a frame, you should change it to 'DENY'.

SECURE_CONTENT_TYPE_NOSNIFF = True
# You should consider enabling this header to prevent the browser from identifying content types incorrectly.
# If not set to True, your pages will not be served with an 'X-Content-Type-Options: nosniff' header.

APPEND_SLASH = True

prod_db = dj_database_url.config(conn_max_age=500)

DATABASES = {}

DATABASES['default'].update(prod_db)
