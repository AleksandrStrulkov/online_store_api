from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsActiveSelf, IsSelfOrSuperuser
from users.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    """CRUD для пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Разрешение только для активного пользователя
        if self.action == "create":
            return [AllowAny()]
        base_permissions = [IsActiveSelf()]

        # Изменение и удаление разрешаем только суперпользователю или владельцу
        if self.action in ["update", "partial_update", "destroy"]:
            return base_permissions + [IsSelfOrSuperuser()]
        return base_permissions

    def perform_create(self, serializer):
        serializer.save()
