#code for admin.py
from django.contrib import admin

from .models import Product,Stock

#class ProductAdmin(admin.ModelAdmin):
#    list_display = ('id','name', 'description')
admin.site.register(Product)

#class StockAdmin(admin.ModelAdmin):
#    list_display = ('product_id','name', 'description','price','quantity')
admin.site.register(Stock)
