from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import Tag, Startup, NewsLink


class TagSerializer(HyperlinkedModelSerializer):
    """Serializer for tags"""

    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug',
                'view_name': 'api-tag-detail',
            }
        }


class StartupSerializer(ModelSerializer):
    """Serializer for startups"""

    class Meta:
        model = Startup
        fields = '__all__'

    tags = TagSerializer(many=True)


class NewsLinkSerializer(ModelSerializer):
    """Serializer for news links"""

    class Meta:
        model = NewsLink
        fields = '__all__'

    startup = StartupSerializer()
