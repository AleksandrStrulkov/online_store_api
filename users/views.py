from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsActiveSelf, IsSelfOrSuperuser
from users.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    """CRUD для пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permission(self):
        # Разрешение только для активного пользователя
        base_permissions = [IsActiveSelf]

        # Изменение и удаление разрешаем только суперпользователю или владельцу
        if self.action in ["update", "partial_update", "destroy"]:
            return base_permissions + [IsSelfOrSuperuser()]
        return base_permissions

    def perform_create(self, serializer):
        # Хеширование пароля
        user = serializer.save()
        user.set_password(user.password)
        user.save()
