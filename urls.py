#Local Imports
from apps.wildlife.views import index

# Django Imports
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wolfscout.views.home', name='home'),
    # url(r'^wolfscout/', include('wolfscout.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # ROOT DIR #
    url(r'^$', index),
)

urlpatterns += staticfiles_urlpatterns()