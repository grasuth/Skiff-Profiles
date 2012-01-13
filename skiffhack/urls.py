from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'demo.html'}),
    (r'^browserid/', include('django_browserid.urls')),
    url(r'^admin/', include(admin.site.urls)),
)