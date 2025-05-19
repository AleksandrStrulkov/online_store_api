from rest_framework.generics import CreateAPIView, ListAPIView

from online_store.serializers import LinkNetworkSerializer


class LinkNetworkCreateAPIView(CreateAPIView):
    serializer_class = LinkNetworkSerializer


class LinkNetworkListAPIView(ListAPIView):
    serializer_class = LinkNetworkSerializer
    queryset = LinkNetwork.objects.all()