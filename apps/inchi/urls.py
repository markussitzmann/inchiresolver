from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from inchi import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'inchis', views.InchiViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'entrypoints', views.EntryPointViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]