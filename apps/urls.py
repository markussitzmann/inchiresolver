from django.conf.urls import patterns, include, url
from django.contrib import admin

import inchi.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^inchi-resolver/', include(inchi.urls)),
    url(r'^inchi-resolver/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)