from django.conf.urls import include, url
from django.contrib import admin

import inchi.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inchi-resolver/', include(inchi.urls)),
    url(r'^inchi-resolver/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
