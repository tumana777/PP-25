from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy

from core.forms import ProductForm
from core.models import Product
from django.views.generic import ListView, CreateView, UpdateView

# def index(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     products = Product.objects.values()
#     return JsonResponse({"products": list(products)})

# def index(request):
#     products = Product.objects.all().select_related('category')
#     total_products = products.count()
#
#     context = {
#         'products': products,
#         'total_products': total_products,
#     }
#
#     return render(request, 'index.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.all().select_related('category')
    ordering = ['-created_at']

    # def get_queryset(self):
    #     return Product.objects.all().select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_products'] = self.get_queryset().count()
        return context

def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'product_detail.html', {'product': product})

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect("core:index")
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form': form})

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('core:index')

# def update_product(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#
#         if form.is_valid():
#             form.save()
#             return redirect("core:product_detail", product_pk=product_pk)
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'update_product.html', {'form': form})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('core:index')
    pk_url_kwarg = 'product_pk'

def delete_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == "POST":
        product.delete()
        return redirect("core:index")
    return redirect("core:index")


def about(request):
    return render(request, 'about.html')