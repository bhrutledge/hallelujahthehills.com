import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hth.settings.local'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

