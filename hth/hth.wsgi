import os, sys
sys.path.append('/Users/brian/Code/django-debugged')
sys.path.append('/Users/brian/lib/python')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hth.settings.local'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
