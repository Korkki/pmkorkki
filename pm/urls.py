from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^api/', include('todo.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
