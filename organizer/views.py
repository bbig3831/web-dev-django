from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer
from .models import Tag, Startup, NewsLink


class TagList(ListView):
    """Display a list of Tags"""

    queryset = Tag.objects.all()
    template_name = 'tag/list.html'


class TagDetail(DetailView):
    """Display a single Tag"""

    queryset = Tag.objects.all()
    template_name = 'tag/detail.html'


class TagApiDetail(RetrieveAPIView):
    """Return JSON for single Tag object"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class TagApiList(ListAPIView):
    """Return JSON for multiple Tag objects"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StartupAPIDetail(RetrieveAPIView):
    """"""

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = 'slug'


class StartupAPIList(ListAPIView):
    """Return JSON for multiple Startup objects"""

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class NewsLinkAPIDetail(RetrieveAPIView):
    """Return JSON for single NewsLink object"""

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):
        """Override DRF's generic method"""
        startup_slug = self.kwargs.get('startup_slug')
        newslink_slug = self.kwargs.get('newslink_slug')
        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug
        )
        self.check_object_permissions(
            self.request, newslink
        )
        return newslink


class NewsLinkAPIList(ListAPIView):
    """Return JSON for multiple NewsLink objects"""

    queryset =  NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
