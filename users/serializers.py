from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Users"""

    class Meta:
        model = User
        fields = (
            "id",
            "last_name",
            "first_name",
            "email",
            "phone",
            "is_active",
            "is_superuser",
            "is_staff",
        )

    def get_fields(self):
        fields = super().get_fields()
        user = self.context["request"].user

        # Только суперпользователь может менять поля 'is_active', 'is_superuser', 'is_staff'
        if not user.is_superuser:
            fields["is_active"].read_only = True
            fields["is_superuser"].read_only = True
            fields["is_staff"].read_only = True

        return fields

    def validate(self, attrs):
        # Вывод сообщения если пользователь пытается изменить поля 'is_active', 'is_superuser', 'is_staff'
        user = self.context["request"].user
        fields = ["is_active", "is_superuser", "is_staff"]
        errors = {}

        if not user.is_superuser:
            for field in fields:
                if field in self.initial_data:
                    errors[field] = f"Только администратор может изменять поле '{field}'."

        if errors:
            raise serializers.ValidationError(errors)

        return attrs
