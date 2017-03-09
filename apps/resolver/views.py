from rest_framework import viewsets, permissions

from resolver.models import Inchi, Organization, Publisher, EntryPoint
from resolver.serializers import InchiSerializer, OrganizationSerializer, \
    PublisherSerializer, EntryPointSerializer


class InchiViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Inchi.objects.all()
    serializer_class = InchiSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class OrganizationViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class PublisherViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class EntryPointViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = EntryPoint.objects.all()
    serializer_class = EntryPointSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

