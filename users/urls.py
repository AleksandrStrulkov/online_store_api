from users.apps import UsersConfig
from rest_framework import routers

from users.views import UsersViewSet

app_name = UsersConfig.name

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet, basename='пользователи')

urlpatterns = [

] + router.urls
