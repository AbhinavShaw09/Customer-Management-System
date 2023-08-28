from rest_framework import serializers
from app.models import(
    CustomersModel,
    OrderModel,
    Product,
    ProductModel
)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomersModel
        fields = '__all__'

class OrderModel(serializers.ModelSerializer):
    class Meta:
        model = OrdersModel
        field = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = '__all__'

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        field = '__all__'

