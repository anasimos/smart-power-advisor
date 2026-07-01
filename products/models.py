from django.db import models


class Product(models.Model):
    PRODUCT_TYPES = (
        ("UPS", "UPS"),
        ("Generator", "Generator"),
        ("Battery", "Battery"),
        ("Solar Panel", "Solar Panel"),
        ("Control Panel", "Control Panel"),
        ("Other", "Other"),
    )

    external_id = models.CharField(max_length=100, unique=True)

    name = models.CharField(max_length=255)

    product_type = models.CharField(
        max_length=50,
        choices=PRODUCT_TYPES,
        default="Other",
    )

    internal_reference = models.CharField(
        max_length=100,
        blank=True,
    )

    description = models.TextField(blank=True)

    weight = models.FloatField(default=0)

    power_kw = models.FloatField(null=True, blank=True)

    power_kva = models.FloatField(null=True, blank=True)

    stock = models.PositiveIntegerField(default=0)

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name