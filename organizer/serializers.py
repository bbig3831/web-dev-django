from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer

from .models import Tag, Startup, NewsLink


class TagSerializer(ModelSerializer):
    """Serializer for tags"""

    url = HyperlinkedIdentityField(view_name='api-tag-detail')

    class Meta:
        model = Tag
        fields = '__all__'


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
