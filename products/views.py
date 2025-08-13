from django.shortcuts import render
from .models import Product

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
