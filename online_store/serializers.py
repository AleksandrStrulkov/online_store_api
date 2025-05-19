from rest_framework import serializers

from online_store.models import LinkNetwork


class LinkNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkNetwork
        fields = '__all__'
