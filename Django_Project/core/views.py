from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.db.models import Q

from core.forms import ProductForm
from core.models import Product, Category
from django.views.generic import (
    ListView, CreateView, UpdateView,
    DetailView, DeleteView
)

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    # queryset = Product.objects.all().select_related('category')
    # ordering = ['-created_at']
    # paginate_by = 3

    def get_queryset(self):
        products = Product.objects.all().select_related('category').order_by('-created_at')

        search_query = self.request.GET.get('q')
        category_name = self.request.GET.get('category')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if search_query:
            products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

        if category_name:
            products = products.filter(category__name=category_name)

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_products'] = self.get_queryset().count()
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    pk_url_kwarg = 'product_pk'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('core:index')
    login_url = 'user:login'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    pk_url_kwarg = 'product_pk'

    def get_success_url(self):
        return reverse_lazy('core:product_detail', kwargs={'product_pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    pk_url_kwarg = 'product_pk'
    success_url = reverse_lazy('core:index')

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

# def product_detail(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#     return render(request, 'product_detail.html', {'product': product})

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

# def delete_product(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#     if request.method == "POST":
#         product.delete()
#         return redirect("core:index")
#     return redirect("core:index")

# def about(request):
#     return render(request, 'about.html')

# class AboutView(TemplateView):
#     template_name = 'about.html'