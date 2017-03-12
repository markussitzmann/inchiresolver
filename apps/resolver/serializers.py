from rest_framework import serializers


from resolver.models import Inchi, Organization, Publisher, EntryPoint


class InchiSerializer(serializers.HyperlinkedModelSerializer):

    _self = serializers.HyperlinkedIdentityField(view_name='inchi-detail', format='html')
    _uid = serializers.UUIDField(source='uid', read_only=True)

    class Meta:
        model = Inchi
        fields = ('_uid', '_self', 'string', 'key', 'version', 'is_standard')
        read_only_fields = ('version', 'is_standard')

    def create(self, validated_data):
        inchi = Inchi.create(**validated_data)
        inchi.save()
        return inchi
        

        
class OrganizationSerializer(serializers.HyperlinkedModelSerializer):

    _self = serializers.HyperlinkedIdentityField(view_name='organization-detail', format='html')

    class Meta:
        model = Organization
        fields = ('_self', 'parent', 'name', 'abbreviation', 'url', 'added', 'modified')

    def create(self, validated_data):
        organization = Organization.create(**validated_data)
        organization.save()
        return organization


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
