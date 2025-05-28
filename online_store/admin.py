from django.contrib import admin

from online_store.models import LinkNetwork


# admin action, очищающий задолженность перед поставщиком у выбранных объектов
@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt_for_supplier(linknetworkadmin, request, queryset):
    queryset.update(debt_for_supplier=0.00)


# Регистрация модели
@admin.register(LinkNetwork)
class LinkNetworkAdmin(admin.ModelAdmin):
    list_display = (
        "hierarchy_name",
        "title",
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "product_name",
        "product_model",
        "product_date",
        "supplier",
        "debt_for_supplier",
        "data_create",
    )
    list_display_links = ("supplier", "hierarchy_name")  # добавление полей в список ссылок
    search_fields = ("city",)
    list_filter = ("city",)
    list_editable = ("debt_for_supplier",)
    actions = [clear_debt_for_supplier]  # добавление действия admin action в меню действий
