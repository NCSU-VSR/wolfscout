from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from resources import CollarResource, CollarDataResource

urlpatterns = patterns('',

    #Collars
    url(r'rest/collarResource/$', ListOrCreateModelView.as_view(resource=CollarResource), name='collar-root'),
    url(r'^rest/collarResource/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=CollarResource)),

    #Collar Data Points
    url(r'rest/collarDataResource/$', ListOrCreateModelView.as_view(resource=CollarDataResource), name='collar-data-root'),
    url(r'^rest/collarDataResource/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=CollarDataResource)),
)