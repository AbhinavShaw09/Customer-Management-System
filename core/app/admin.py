from django.contrib import admin

from .models import(
    CustomersModel,
    OrdersModel,
    Products,
    ProductModel

)

admin.site.register(CustomersModel)
admin.site.register(OrdersModel)
admin.site.register(Products)
admin.site.register(ProductModel)