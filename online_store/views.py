from django_filters import rest_framework as filters
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from online_store.models import LinkNetwork
from online_store.permissions import IsActiveUser, IsOwnerOrSuperuser
from online_store.serializers import LinkNetworkSerializer


class LinkNetworkCreateAPIView(CreateAPIView):
    """Создание нового звена сети"""

    serializer_class = LinkNetworkSerializer
    permission_classes = [IsActiveUser]

    def perform_create(self, serializer):
        # Сохранение нового звена сети и указываем владельца
        new_network = serializer.save()
        new_network.owner = self.request.user

        new_network.save()


class LinkNetworkListAPIView(ListAPIView):
    """Просмотр списка звеньев сети"""

    serializer_class = LinkNetworkSerializer
    queryset = LinkNetwork.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["city"]
    permission_classes = [IsActiveUser]


class LinkNetworkRetrieveAPIView(RetrieveAPIView):
    """Просмотр звена сети"""

    serializer_class = LinkNetworkSerializer
    queryset = LinkNetwork.objects.all()
    permission_classes = [IsActiveUser, IsOwnerOrSuperuser]


class LinkNetworkUpdateAPIView(UpdateAPIView):
    """Изменение звена сети"""

    serializer_class = LinkNetworkSerializer
    queryset = LinkNetwork.objects.all()
    permission_classes = [IsActiveUser, IsOwnerOrSuperuser]


class LinkNetworkDestroyAPIView(DestroyAPIView):
    """Удаление звена сети"""

    queryset = LinkNetwork.objects.all()
    permission_classes = [IsActiveUser, IsOwnerOrSuperuser]
