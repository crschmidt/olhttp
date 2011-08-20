from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^data/(?P<type>[A-Za-z]*)/$', 'data', name='data'),
    url(r'^data/(?P<type>[A-Za-z]*)/(?P<id>[0-9]*)$', 'data', name='data'),
    url(r'^ui/$', 'ui', name='ui'),
)    
