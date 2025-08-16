from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer

def product_list(request):
    category = request.GET.get('category', 'car_diecast')
    categories = dict(Product.CATEGORY_CHOICES)

    products = Product.objects.filter(category=category, active=True)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'product_list.html', context)


class ProductListAPIView(APIView):
    def get(self, request, format=None):
        category = request.query_params.get("category", "car_diecast")
        categories = dict(Product.CATEGORY_CHOICES)

        products = Product.objects.filter(category=category, active=True)
        serializer = ProductSerializer(products, many=True)

        return Response({
            "products": serializer.data,
            "categories": categories,
            "selected_category": category,
        })
