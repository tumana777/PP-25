from django.urls import path
from core.views import index, about, product_detail

app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/<int:product_pk>/', product_detail, name='product_detail'),
]