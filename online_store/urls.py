from django.urls import path

from online_store.apps import OnlineStoreConfig
from online_store.views import (LinkNetworkCreateAPIView,
                                LinkNetworkDestroyAPIView,
                                LinkNetworkListAPIView,
                                LinkNetworkRetrieveAPIView,
                                LinkNetworkUpdateAPIView)

app_name = OnlineStoreConfig.name

urlpatterns = [
    path("network/create/", LinkNetworkCreateAPIView.as_view(), name="network_create"),
    path("network/", LinkNetworkListAPIView.as_view(), name="network_list"),
    path("network/<int:pk>/", LinkNetworkRetrieveAPIView.as_view(), name="network_get"),
    path("network/update/<int:pk>/", LinkNetworkUpdateAPIView.as_view(), name="network_update"),
    path("network/delete/<int:pk>/", LinkNetworkDestroyAPIView.as_view(), name="network_delete"),
]
