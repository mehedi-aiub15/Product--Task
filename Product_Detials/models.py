from django.db import models
from rest_framework import serializers


# Create your models here.
class Product(models.Model):
    #id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return str(self.id)
class Stock(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()
    def __str__(self):
        return str(self.product)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('product', 'name', 'description', 'price','quantity')
