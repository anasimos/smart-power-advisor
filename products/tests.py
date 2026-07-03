
from django.test import TestCase

from products.models import Product
from products.services import ProductService


class ProductServiceTests(TestCase):

    def setUp(self):
        Product.objects.create(
            external_id="UPS001",
            internal_reference="UPS001",
            name="UPS-UA1500VA",
            product_type="Goods",
            description="1500VA UPS",
            active=True,
            stock=10,
            price=100,
        )

    def test_search_returns_matching_product(self):
        products = ProductService.search("1500")

        self.assertEqual(products.count(), 1)
        self.assertEqual(products.first().name, "UPS-UA1500VA")