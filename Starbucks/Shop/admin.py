from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'customer_name', 'email', 'phone', 'size', 'created_at']
    list_filter = ['created_at']  # Ensure this field exists in the model

    def size(self, obj):
        return obj.size

    def created_at(self, obj):
        return obj.created_at
