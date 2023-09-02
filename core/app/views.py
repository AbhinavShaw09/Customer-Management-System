from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import(
    CustomerModel,
    OrderModel,
    Product,
    ProductModel
)
from .serializers import(
    CustomerSerializer,
    OrderModelSerializer,
    ProductSerializer,
    ProductModelSerializer
)


class CustomerViewSet(ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class =   CustomerSerializer
    # permission_class = [IsAuthenticated]

class OrderModelViewSet(ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class =   OrderModelSerializer
    # permission_class = [IsAuthenticated]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class =   ProductSerializer
    # permission_class = [IsAuthenticated]

class ProductModelViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class =   ProductModelSerializer
    # permission_class = [IsAuthenticated]