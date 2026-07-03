from django.db.models import Q
from .models import Product


class ProductService:

    @staticmethod
    def search(query):
        return Product.objects.filter(
            active=True
        ).filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(external_id__icontains=query) |
            Q(internal_reference__icontains=query)
        )