from rest_framework import serializers


from inchi.models import Inchi, Organization, Publisher, EntryPoint


class InchiSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Inchi
        fields = ('id', 'key', 'string',)
        

        
class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    
    _self = serializers.HyperlinkedIdentityField(view_name='organization-detail', format='html')
    
    class Meta:
        model = Organization
        fields = ('_self', 'parent', 'name', 'abbreviation', 'url', 'added', 'modified')
        

        
class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    
    _self = serializers.HyperlinkedIdentityField(view_name='publisher-detail', format='html', )
    organization = serializers.HyperlinkedRelatedField(queryset=Organization.objects.all(), view_name='organization-detail',)

    class Meta:
        model = Publisher
        fields = ('_self', 'parent', 'organization', 'name', 'group', 'contact', 'url', 'added', 'modified')
        


class EntryPointSerializer(serializers.HyperlinkedModelSerializer):
    
    _self = serializers.HyperlinkedIdentityField(view_name='entrypoint-detail', format='html', )
    publisher = serializers.HyperlinkedRelatedField(queryset=Publisher.objects.all(), view_name='publisher-detail',)

    class Meta:
        model = EntryPoint
        fields = ('_self', 'publisher', 'url', 'description')
