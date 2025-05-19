from django.urls import path

from rest_framework import routers
from online_store.apps import OnlineStoreConfig
from online_store.views import LinkNetworkCreateAPIView

app_name = OnlineStoreConfig.name

urlpatterns = [
    path('network/create/', LinkNetworkCreateAPIView.as_view(), name='network_create'),

]

