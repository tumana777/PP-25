from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from core.models import Product, Category
from .serializers import CategorySerializer, ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

# @api_view(['GET', 'POST'])
# def product_list(request):
#     products = Product.objects.values().order_by('-created_at')
#     return Response(products)

# @api_view()
# def category_list(request):
#     categories = Category.objects.all().annotate(total_products=Count('products'))
#     serializer = CategorySerializer(categories, many=True)
#     return Response(serializer.data)
#
# @api_view()
# @permission_classes([IsAuthenticated])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True, context={'request': request})
#     return Response(serializer.data)

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticated]

class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateSerializer