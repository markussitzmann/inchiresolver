from django.conf.urls import include, url
from django.contrib import admin

import inchi.urls

urlpatterns = [
    url(r'^', include(inchi.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
