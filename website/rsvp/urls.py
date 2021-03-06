from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'event.views.home', name='home'),
    url(r'^events/$', 'event.views.all_events', name='all events'),
    url(r'^register/$', 'event.views.register', name='register'),
    url(r'^api/get_events/$', 'event.views.get_events', name='get events'),
    url(r'^api/post_event/$', 'event.views.post_event', name='get events'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
