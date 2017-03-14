from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

import resolver.urls

schema_view = get_swagger_view(title='Test API')

urlpatterns = [
    url(r'^', include(resolver.urls)),
    url(r'^openapi/', schema_view),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
