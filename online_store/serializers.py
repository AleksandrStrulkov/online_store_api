from rest_framework import serializers

from online_store.models import LinkNetwork


class LinkNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkNetwork
        fields = '__all__'

    def update(self, instance, validated_data):
        if "debt_for_supplier" in validated_data:
            raise serializers.ValidationError({'debt_for_supplier': 'Обновление данного поля запрещено.'})
        return super().update(instance, validated_data)
