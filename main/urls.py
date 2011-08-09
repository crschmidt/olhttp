from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^data/$', 'data', name='data'),
    url(r'^data/(?P<id>[0-9])/$', 'data', name='data'),
)    
