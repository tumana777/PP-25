from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from core.models import Product, Category
from .serializers import (
    CategorySerializer, ProductListSerializer, ProductDetailSerializer,
    ProductCreateSerializer, ProductUpdateSerializer
)
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

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
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductListSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticated]

class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductListSerializer

    # def get_permissions(self):
    #     if self.request.method == "POST":
    #         return [IsAuthenticated()]
    #     return [AllowAny()]

class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProductUpdateSerializer
        return ProductDetailSerializer