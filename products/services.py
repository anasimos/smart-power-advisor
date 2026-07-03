from .models import Product


class ProductService:

    @staticmethod
    def search(query):
        return Product.objects.filter(
            name__icontains=query,
            active=True,
        )

    @staticmethod
    def get_by_external_id(external_id):
        return Product.objects.filter(
            external_id=external_id
        ).first()