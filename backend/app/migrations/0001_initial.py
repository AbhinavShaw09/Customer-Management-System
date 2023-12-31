# Generated by Django 4.2.4 on 2023-08-30 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('cus_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('delivery_due_date', models.DateField(auto_created=True)),
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('invoice_creation_da', models.CharField(blank=True, max_length=100, null=True)),
                ('custom_message', models.TextField(blank=True, null=True)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app.customermodel')),
            ],
            options={
                'verbose_name': 'Orders',
                'db_table': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('order_product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('order_model_pm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderId', to='app.ordermodel')),
                ('product_pm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productId', to='app.product')),
            ],
            options={
                'verbose_name': 'ProductModel',
                'verbose_name_plural': 'ProductModels',
                'db_table': 'ProductModel',
            },
        ),
    ]
