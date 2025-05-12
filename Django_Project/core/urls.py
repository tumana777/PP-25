from django.urls import path
from core.views import (
    about, product_detail, delete_product,
    ProductListView, ProductCreateView, ProductUpdateView
)

app_name = 'core'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('product/<int:product_pk>/', product_detail, name='product_detail'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('update_product/<int:product_pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:product_pk>/', delete_product, name='delete_product'),
]