from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .services import ProductService


@api_view(["GET"])
def search_products(request):
    query = request.GET.get("q", "")

    products = ProductService.search(query)

    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)
