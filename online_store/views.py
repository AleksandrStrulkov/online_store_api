from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django_filters import rest_framework as filters
from online_store.models import LinkNetwork
from online_store.serializers import LinkNetworkSerializer


class LinkNetworkCreateAPIView(CreateAPIView):
    serializer_class = LinkNetworkSerializer


class LinkNetworkListAPIView(ListAPIView):
    serializer_class = LinkNetworkSerializer
    queryset = LinkNetwork.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['city']


class LinkNetworkRetrieveAPIView(RetrieveAPIView):
    serializer_class = LinkNetworkSerializer
    queryset = LinkNetwork.objects.all()


class LinkNetworkUpdateAPIView(UpdateAPIView):
    serializer_class = LinkNetworkSerializer
    queryset = LinkNetwork.objects.all()


class LinkNetworkDestroyAPIView(DestroyAPIView):
    queryset = LinkNetwork.objects.all()
