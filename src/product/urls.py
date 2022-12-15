from django.urls import path

from product.views.product import CreateProductView, ProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView

app_name = "product"



urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', ProductView.as_view(), name='list.product'),
    # path('list/', TemplateView.as_view(
    #     template_name='products/list.html', 
    #     extra_context={
    #         'products': Product.objects.prefetch_related('ProductVariantPrice'),
    #         'paginators': Paginator(Product.objects.prefetch_related('ProductVariantPrice'), per_page=2),
    #     }
    # ), name='list.product'),
]

