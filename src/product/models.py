from django.db import models
from config.g_model import TimeStampMixin
from django.core.exceptions import ValidationError


# Create your models here.
class Variant(TimeStampMixin):
    title = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        if self.title:
            return f"{self.title}"
        else:
            return "NO_TITLE"
    
    def clean(self) -> None:
        if not self.title:
            raise ValidationError("Title cannot be null or empty")
        return super().clean()

    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super(Variant, self).save(*args, **kwargs)


class Product(TimeStampMixin):
    title = models.CharField(max_length=255, null=True, blank=True)
    sku = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        if self.title and self.sku:
            return f"{self.title} - {self.sku}"
        elif self.title and not self.sku:
            return f"{self.sku} - NO_SKU"
        elif not self.title and self.sku:
            return f"NO_TITLE - {self.sku}"
        else:
            return "NO_TITLE - NO_SKU"
    
    def clean(self) -> None:
        if not self.title:
            raise ValidationError("Title cannot be null or empty")
        if not self.sku:
            raise ValidationError("sku cannot be null or empty")
        return super().clean()
    
    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super(Product, self).save(*args, **kwargs)


class ProductVariant(TimeStampMixin):
    variant_title = models.CharField(max_length=255, null=True, blank=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        if self.variant_title:
            return f"{self.variant_title}"
        else:
            return "NO_VARIENT_TITLE"
    
    def clean(self) -> None:
        if not self.variant_title:
            raise ValidationError("variant_title cannot be null or empty")
        if not self.variant:
            raise ValidationError("varient relation cannot be empty")
        if not self.product:
            raise ValidationError("product relation cannot be empty")
        return super().clean()

    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super(ProductVariant, self).save(*args, **kwargs)


class ProductImage(TimeStampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    file_path = models.URLField(max_length=255, null=True, blank=True)
    thumbnail = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        if self.product:
            return f"{self.product.title}"
        else:
            return "NO_PRODUCT_IMAGE_NAME"
    
    def clean(self) -> None:
        if not self.file_path:
            raise ValidationError("file_path cannot be null or empty")
        if not self.thumbnail:
            raise ValidationError("thumbnail cannot be null or empty")
        if not self.product:
            raise ValidationError("product relation cannot be empty")
        return super().clean()

    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super(ProductImage, self).save(*args, **kwargs)


class ProductVariantPrice(TimeStampMixin):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, related_name='product_variant_three')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        if self.product and self.price:
            return f"{self.product} - {self.price}"
        else:
            return "NO_PRODUCT_VARIENT_PRICE"
    
    def clean(self) -> None:
        if not self.price:
            raise ValidationError("price cannot be null or empty")
        if not self.stock:
            raise ValidationError("stock cannot be null or empty")
        if not self.product:
            raise ValidationError("product relation cannot be empty")
        return super().clean()

    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super(ProductVariantPrice, self).save(*args, **kwargs)

