from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {"blank": True, "null": True}


class LinkNetwork(models.Model):
    """Модель сети по продаже электроники"""

    HIERARCHY_NAME = (
        ("Завод", "Завод"),
        ("Розничная сеть", "Розничная сеть"),
        ("ИП", "ИП"),
    )

    hierarchy_name = models.CharField(max_length=20, verbose_name="Тип звена иерархии", choices=HIERARCHY_NAME)
    title = models.CharField(
        max_length=50,
        verbose_name="Название",
    )
    email = models.EmailField(verbose_name="Электронная почта", max_length=100, unique=True)
    country = models.CharField(max_length=15, verbose_name="Страна", default="Россия")
    city = models.CharField(max_length=15, verbose_name="Город")
    street = models.CharField(max_length=20, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    product_name = models.CharField(max_length=50, verbose_name="Наименование товара")
    product_model = models.CharField(
        max_length=15,
        verbose_name="Модель товара",
    )
    product_date = models.DateField(verbose_name="Дата выхода на рынок")
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Поставщик",
        **NULLABLE,
    )
    debt_for_supplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком",
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, **NULLABLE)
    data_create = models.DateField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.hierarchy_name} - {self.title}"

    class Meta:
        verbose_name = "звено продажи"
        verbose_name_plural = "звенья продажи"
        ordering = ["title"]
