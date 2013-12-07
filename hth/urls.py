from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

from debugged.posts.feeds import PostsFeed
from debugged.calendar.feeds import CalendarFeed

feeds = {
    'news': PostsFeed,
    'calendar': CalendarFeed,
}

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^calendar/',  include('debugged.calendar.urls')),
    (r'^music/',  include('debugged.discography.urls')),
    (r'^news/',  include('debugged.posts.urls')),
    (r'^', include('debugged.bandsite.urls')),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home_page.html'}, name='home'),
    url(r'^about/$', 'django.views.generic.simple.direct_to_template', {'template': 'about_page.html'}, name='about'),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}, name='feeds'),
)

legacy_urls = [
    (r'^mp3s/(?P<file>.*)', '/files/songs/%(file)s'),
    (r'^0972/(?P<file>.*)', '/files/0972/%(file)s'),
    (r'^band\.html', 'about'),
    (r'^music\.html', 'music'),
    (r'^shows\.html', 'calendar'),
    (r'^press\.html', 'press'),
    (r'^merch\.html', 'music'),
    (r'^contact\.html', 'contact'),
    (r'^drones\.html', '/music/releases/colonial-drones'),
    (r'^ptq\.html', '/music/releases/prepare-to-qualify'),
    (r'^cpb\.html', '/music/releases/collective-psychosis-begone'),
    (r'^portal\.html', '/music/portal'),
    (r'^flyers.*html', '/calendar/posters'),
    (r'^photos.*html', '/photos'),
    (r'^news\.[xml|rss]', '/feeds/news'),
    (r'^shows\.[xml|rss]', '/feeds/calendar'),
]

for old_url, new_url in legacy_urls:
    urlpatterns += patterns('', 
        (old_url, 'django.views.generic.simple.redirect_to', {'url': new_url}))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)        
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
