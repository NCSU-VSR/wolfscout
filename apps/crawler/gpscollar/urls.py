from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from resources import CollarResource, CollarDataResource
from views import ExampleView, AnotherExampleView
urlpatterns = patterns('',

    #CollarDataFilterByDate
    url(r'^restDemo/$', ExampleView.as_view(), name='example-resource'),
    url(r'^restDemo/(?P<num>[0-9]+)/$', AnotherExampleView.as_view(), name='another-example'),

    #Collars
    url(r'rest/collarResource/$', ListOrCreateModelView.as_view(resource=CollarResource), name='collar-root'),
    url(r'^rest/collarResource/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=CollarResource)),

    #Collar Data Points
    url(r'rest/collarDataResource/$', ListOrCreateModelView.as_view(resource=CollarDataResource), name='collar-data-root'),
    url(r'^rest/collarDataResource/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=CollarDataResource)),
)