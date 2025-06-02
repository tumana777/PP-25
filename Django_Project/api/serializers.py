from rest_framework import serializers

from core.models import Product, Category


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     saxeli = serializers.CharField(source='name')
#     total_products = serializers.IntegerField()

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     price = serializers.FloatField()
#     category = serializers.CharField()
#     quantity = serializers.IntegerField()
#     available = serializers.BooleanField()
#     description = serializers.CharField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     image = serializers.ImageField()
#     views = serializers.IntegerField()

class CategorySerializer(serializers.ModelSerializer):

    saxeli = serializers.CharField(source='name')
    # total_products = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id', 'saxeli')

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')

class ProductDetailSerializer(serializers.ModelSerializer):

    mtliani_fasi = serializers.SerializerMethodField(method_name='total_price')
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ('available', 'views')

    def total_price(self, obj):
        return obj.price * obj.quantity

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'quantity', 'description', 'category', 'image')