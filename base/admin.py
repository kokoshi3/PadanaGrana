from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'image']
    search_fields = ['name', 'description']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
