from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "power_kw",
        "power_kva",
        "stock",
        "price",
        "active",
    )

    search_fields = (
        "name",
        "external_id",
        "internal_reference",
    )

    list_filter = (
        "category",
        "active",
    )
