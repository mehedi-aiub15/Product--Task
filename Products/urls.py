from django.contrib import admin
from django.urls import path,include

from Product_Detials import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/v1/products/',views.product_collection),
    path('api/v1/products/<int:pk>/',views.product_element),
    path('api/v1/stock/',views.stock_collection),
    path('api/v1/stock/<int:pk>/',views.stock_element),
]
