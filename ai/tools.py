from products.services import ProductService
from calculators.load import LoadCalculator


def search_products(query):
    products = ProductService.search(query)

    results = []

    for product in products[:5]:
        results.append({
            "name": product.name,
            "description": product.description,
            "stock": product.stock,
            "price": float(product.price),
        })

    return results


def calculate_load(devices):
    """
    devices example:
    [
        ("desktop computer", 3),
        ("printer", 2),
    ]
    """
    return LoadCalculator.calculate(devices)