from .models import Product


class RecommendationService:

    @staticmethod
    def recommend_ups(required_watts):

        return (
            Product.objects
            .filter(
                active=True,
                name__icontains="UPS",
                power_watts__gte=required_watts,
            )
            .order_by("power_watts")
            .first()
        )