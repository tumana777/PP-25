from django.urls import path
from .views import CategoryListView, ProductListView, ProductDetailView, ProductCreateView

app_name = 'api'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
]