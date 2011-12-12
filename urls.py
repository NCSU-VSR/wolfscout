#Local Imports
from apps.general.views import index
from shapes import views
# Django Imports
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
#Import The CollarData URLS
from apps.crawler.gpscollar import urls
from apps.crawler.gpscollar.models import *
# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin

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

    url(r'^export_animal/$', 'wolfscout.apps.wildlife.views.export'),
    url(r'^export_collar/$', 'wolfscout.apps.crawler.gpscollar.views.export'),
    url(r'^export_interactions/$', 'wolfscout.apps.study.views.interactions'),
    url(r'^export_interactions/(?P<theStudyID>\d+)/$', 'wolfscout.apps.study.views.getInteractionGroups'),
    url(r'^export_interactions/group/(?P<theGroupID>\d+)/$', 'wolfscout.apps.study.views.getGroupInteractions'),

    url(r'^collar_data_upload/$', 'wolfscout.apps.crawler.gpscollar.views.uploadCSVToProcess'),
    url(r'^collar_data/(?P<theCollarID>\d+)/$', 'wolfscout.apps.crawler.gpscollar.views.getCollarData'),
    url(r'^upload_collar/$', 'wolfscout.apps.crawler.gpscollar.views.uploadCollarDataFile'),
    url(r'^upload_collar_success/$', 'wolfscout.apps.crawler.gpscollar.views.uploadCollarDataFile_Success'),

    url(r'^collarDataKML/(?P<theCollarID>\d+)/$', 'wolfscout.apps.crawler.gpscollar.views.getKMLForAllCollarPoints'),
    url(r'^getInteractionKML/$', 'wolfscout.apps.crawler.gpscollar.views.getKMLForAllCollarPointsInteractions'),

    #url(r'^studies/$', 'wolfscout.apps.study.views.studies'),
    #url(r'^study_add/$', 'wolfscout.apps.study.views.add'),
    #url(r'^study_delete/(?P<theStudyID>\d+)/$', 'wolfscout.apps.study.views.delete'),
    #url(r'^study_edit/(?P<theStudyID>\d+)/$', 'wolfscout.apps.study.views.edit'),
    #url(r'^study/(?P<theStudyID>\d+)/$', 'wolfscout.apps.study.views.study'),
    url(r'^exportShape/$','wolfscout.apps.crawler.gpscollar.views.exportShape'),

)

#Add Static Data
urlpatterns += staticfiles_urlpatterns()


#Add Restful Inteface To CollarData
urlpatterns += urls.urlpatterns

#Downloadable reports
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        }),
    )
