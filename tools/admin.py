from django.contrib import admin
from tools.models import (
    Product,
    Variant,
    Backup,
    ProductType
)


@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'file', 'size']

    def size(self, obj):
        """
        docstring
        """
        return obj.file.size


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'title', 'shopify_id', 'sku']
    search_fields = ['product__handle',
                     'product__product_type', 'product__title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['handle', 'shopify_id',
                    'product_type', 'sku_fixed', 'title']
    list_filter = ['product_type', 'sku_fixed']
    search_fields = ['handle', 'product_type', 'title']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
