from django.db import models

class CustomerModel(models.Model):
    cus_id = models.IntegerField(primary_key=True,blank=False,null=False)
    first_name = models.CharField(max_length=100,blank=False,null=False)
    last_name = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    company = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(blank=False,null=False)

    class Meta:
        db_table = 'Customer'
        verbose_name = 'Customer'

    def __str__(self):
        return self.first_name +' '+ self.last_name
    

class OrderModel(models.Model):
    order_id = models.IntegerField(primary_key=True,blank=False,null=False)
    cust_id  = models.ForeignKey(CustomerModel,on_delete=models.CASCADE,blank=False,null=False,related_name='orders')
    invoice_creation_da = models.CharField(max_length=100,blank=True,null=True)
    delivery_due_date = models.DateField(auto_created=True)
    custom_message = models.TextField(blank=True,null=True)

    class Meta:
        db_table = 'Orders'
        verbose_name = 'Orders'

    def __str__(self):
        return self.invoice_creation_da
    

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True,blank=False,null=False)
    name = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField(blank=False,null=False)

    class Meta:
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
    

class ProductModel(models.Model):
    order_product_id = models.IntegerField(primary_key=True,blank=False,null=False)
    order_id = models.ForeignKey(OrderModel,on_delete=models.CASCADE,blank=False,null=False,related_name='orderId')
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False,related_name='productId')
    quantity = models.IntegerField(blank=False,null=False)
    
    class Meta:
        db_table = 'ProductModel'
        verbose_name = 'ProductModel'
        verbose_name_plural = 'ProductModels'

    def __str__(self):
        return str(self.order_id)
    







        