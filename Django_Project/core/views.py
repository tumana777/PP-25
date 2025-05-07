from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from core.models import Product


# def index(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     products = Product.objects.values()
#     return JsonResponse({"products": list(products)})


def index(request):
    products = Product.objects.all()
    total_products = products.count()

    context = {
        'products': products,
        'total_products': total_products,
    }

    return render(request, 'index.html', context)

def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'product_detail.html', {'product': product})

def about(request):
    return render(request, 'about.html')