from django.urls import path
from .views import (
    CategoryListView, ProductListView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductListCreateView, ProductRetrieveUpdateDeleteView
)

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    # path('products/', ProductListView.as_view(), name='product_list'),
    # path('products/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    # path('add_product/', ProductCreateView.as_view(), name='add_product'),
    # path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('products/', ProductListCreateView.as_view(), name='product_list_create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product_get_update_delete'),
]