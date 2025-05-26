from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Разрешение доступа только активным пользователям"""

    message = "Доступ разрешен только активным пользователям"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active)


class IsOwnerOrSuperuser(BasePermission):
    """Разрешение доступа только владельцу объекта и суперпользователю"""

    message = "У вас нет прав на изменение и удаления этого объекта"

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_superuser:
            return True
        return obj.owner == request.user
