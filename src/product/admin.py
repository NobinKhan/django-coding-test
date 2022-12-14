from django.contrib import admin
from .models import Variant, Product, ProductVariant, ProductImage, ProductVariantPrice


# Register your models here.
@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    list_per_page = 15
    list_filter = ("title", "created_at", "updated_at")
    search_fields = ("id", "title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sku", "created_at", "updated_at")
    list_per_page = 15
    list_filter = ("title", "sku", "created_at", "updated_at")
    search_fields = ("id", "title", "sku")


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("id", "variant_title", "variant", "product", "created_at", "updated_at")
    list_per_page = 15
    list_filter = ("variant_title", "variant", "product", "created_at", "updated_at")
    search_fields = ("id", "variant_title", "variant", "product",)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "thumbnail", "created_at", "updated_at")
    list_per_page = 15
    list_filter = ("product", "thumbnail", "created_at", "updated_at")
    search_fields = ("id", "thumbnail", "product",)


@admin.register(ProductVariantPrice)
class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ("id", "product_variant_one", "product_variant_two", "product_variant_three", "product", "price", "stock")
    list_per_page = 15
    list_filter = ("product", "price", "stock")
    search_fields = ("id", "product_variant_one", "product_variant_two", "product_variant_three", "product", "price", "stock")