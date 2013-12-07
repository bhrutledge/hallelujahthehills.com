from hth.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

SECRET_KEY = 'r8$=cfo@x(pdyldnfb@_64j00%bxd4s_@7i-*=9*5g!ct+lfsn'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/Users/brian/Code/django-debugged/hth/hth.db',
    }
}

TEMPLATE_DIRS = (
    '/Users/brian/Code/django-debugged/hth/templates',
)

STATIC_ROOT = '/Users/brian/Sites/hth_static/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

STATICFILES_DIRS = (
    '/Users/brian/Code/django-debugged/hth/static',
)

MEDIA_ROOT = '/Users/brian/Sites/hth_files/'
MEDIA_URL = '/files/'
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_MAX_UPLOAD_SIZE = 104857600

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'rutt'
EMAIL_HOST_PASSWORD = '3r1cA403'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CACHE_BACKEND = 'dummy://'
