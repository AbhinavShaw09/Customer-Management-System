from django.contrib import admin

from .models import(
    CustomerModel,
    OrderModel,
    Product,
    ProductModel

)

admin.site.register(CustomerModel)
admin.site.register(OrderModel)
admin.site.register(Product)
admin.site.register(ProductModel)