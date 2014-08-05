from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

from un.views import about
from un.views import contact
from un.views import index
from un.views import r_graph


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about', about),
    url(r'^contact', contact),
    url(r'^r/(?P<graph>.*)$', r_graph),
    url(r'^$', index), 
)
