from ai.tools import search_products
from .client import client


class AIService:

    @staticmethod
    def chat(message):

        lower = message.lower()

        if any(word in lower for word in [
            "battery",
            "ups",
            "generator",
            "solar",
            "panel",
        ]):

            products = search_products(message)

            prompt = f"""
Customer asked:

{message}

These are the matching products:

{products}

Answer using ONLY these products.
If no products are listed, say you couldn't find a matching product.
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message,
        )

        return response.text