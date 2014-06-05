from django.conf.urls import patterns, include, url
from django.contrib import admin
from un.views import index


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index), 
)
