#Local Imports
from apps.general.views import index

# Django Imports
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
#Import The CollarData URLS
from apps.crawler.gpscollar import urls
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

	## Authentication ##
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),

    # ROOT DIR #
    url(r'^$', index),	

    url(r'^collar/$', 'wolfscout.apps.crawler.gpscollar.views.collarForm'),
    url(r'^collarDataUpload/$', 'wolfscout.apps.crawler.gpscollar.views.uploadCollarDataFile'),
    url(r'^collarData/(?P<theCollarID>\d+)/$', 'wolfscout.apps.crawler.gpscollar.views.getCollarData'),
    url(r'^collarDataKML/(?P<theCollarID>\d+)/$', 'wolfscout.apps.crawler.gpscollar.views.getKMLForAllCollarPoints'),
    
    url(r'^experiments/$', 'wolfscout.apps.general.views.experiments'),
    url(r'^experiment/(?P<theExperimentID>\d+)/$', 'wolfscout.apps.general.views.experiment'),
)

#Add Static Data
urlpatterns += staticfiles_urlpatterns()

#Add Restful Inteface To CollarData
urlpatterns += urls.urlpatterns

