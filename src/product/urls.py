from django.urls import path
from django.views.generic import TemplateView
from django.db.models import F, ExpressionWrapper, Q, Subquery, Prefetch
from rest_framework import serializers
from product.views.product import CreateProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView
from product.models import  Product, ProductVariantPrice

app_name = "product"



urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', TemplateView.as_view(
        template_name='products/list.html', 
        extra_context={
            'products': Product.objects.prefetch_related('ProductVariantPrice'),
        }
    ), name='list.product'),
]

