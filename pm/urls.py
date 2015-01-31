from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^api/', include('todo.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'$', TemplateView.as_view(template_name='index.html'), name='index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
