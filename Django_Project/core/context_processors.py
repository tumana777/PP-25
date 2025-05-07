from core.models import Product

def global_settings(request):
    products = Product.objects.all()
    return {'products': products}