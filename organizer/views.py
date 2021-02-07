from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TagSerializer
from .models import Tag


class TagApiDetail(APIView):
    """Return JSON for single Tag object"""

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        s_tag = TagSerializer(tag, context={'request': request})
        return Response(s_tag.data)


class TagApiList(APIView):
    """Return JSON for multiple Tag objects"""
    def get(self, request):
        tag_list = get_list_or_404(Tag)
        s_tag = TagSerializer(tag_list, many=True, context={'request': request})
        return Response(s_tag.data)
