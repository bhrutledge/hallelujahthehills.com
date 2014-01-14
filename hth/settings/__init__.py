# Django settings for hth project.

ADMINS = (
    ('Brian Rutledge', 'bhrutledge@gmail.com'),
)

MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = '[HtH] '
SERVER_EMAIL = 'django@hallelujahthehills.com'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'
DATE_FORMAT = 'F j, Y'
DATE_RANGE_YEAR_FORMAT = '(n/j/y) - (n/j/y)'
DATE_RANGE_MONTH_FORMAT = '(n/j) - (n/j, Y)'
DATE_RANGE_DAY_FORMAT = '(F j)-(j, Y)'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'debugged.core.context_processors.current_site',
    'debugged.bandsite.context_processors.forms',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'honeypot.middleware.HoneypotMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

CACHE_MIDDLEWARE_SECONDS = 60 * 10
CACHE_MIDDLEWARE_KEY_PREFIX = 'hth'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

ROOT_URLCONF = 'hth.urls'

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'flatblocks',
    'honeypot',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'debugged.core',
    'debugged.attachments',
    'debugged.contacts',
    'debugged.calendar',
    'debugged.discography',
    'debugged.posts',
    'debugged.bandsite',
    'debugged.management',
)

GRAPPELLI_ADMIN_TITLE = 'Hallelujah The Hills'

FILEBROWSER_SELECT_FORMATS = {
    'File': ['Folder','Image','Document','Audio'],
    'Image': ['Image'],
    'Audio': ['Audio'],
    'Document': ['Document'],
    'image': ['Image'],
    'file': ['Folder','Image','Document','Audio'],
}

FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail', 'width': 150, 'height': 150, 'opts': 'crop'},
    'medium': {'verbose_name': 'Medium', 'width': 480, 'height': '', 'opts': ''},
	'large': {'verbose_name': 'Large', 'width': 800, 'height': 800, 'opts': ''},
}

FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'medium', 'large']
FILEBROWSER_ADMIN_THUMBNAIL = 'fb_thumb'

FILEBROWSER_CONVERT_FILENAME = False

HONEYPOT_FIELD_NAME = 'email'

BANDSITE_CONTACT_EMAILS = [
    {'subject': 'General', 'email': 'ryan@hallelujahthehills.com', 'name': 'Ryan Walsh'},
    #{'subject': 'PR', 'email': 'ever@tinyhuman.com', 'name': 'Ever Kipp, Tiny Human'},
    #{'subject': 'Booking', 'email': 'joe@nicodemusagency.com', 'name': 'Joe Smyth, Nicodemus Agency'},
    #{'subject': 'Website', 'email': 'brian@hallelujahthehills.com'},
]

BANDSITE_LIST_EMAIL = 'hth-list-join@hallelujahthehills.com'

DEBUGGED_CONTACT_TYPES = [('artist', 'Artist'), ('band', 'Band'), ('label', 'Label')]

DEBUGGED_LOCATION_TYPES = [('club', 'Club'), ('festival', 'Festival'), ('gallery', 'Gallery'),
                           ('house', 'House'), ('movie-theater', 'Movie Theater'), 
                           ('radio', 'Radio'), ('record-store', 'Record Store')]
