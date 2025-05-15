from django.urls import path
from django.views.generic import TemplateView

from core.views import (
    ProductListView, ProductCreateView, ProductUpdateView,
    ProductDetailView, ProductDeleteView
)

app_name = 'core'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('product/<int:product_pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('update_product/<int:product_pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:product_pk>/', ProductDeleteView.as_view(), name='delete_product'),
]