from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """Модель пользователя"""

    username = None

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        **NULLABLE,
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        **NULLABLE,
    )
    email = models.EmailField(
        unique=True,
        verbose_name="E-mail",
    )
    phone = models.CharField(max_length=12, verbose_name="Номер телефона", **NULLABLE)
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name="Прошел активацию?")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
