from django.urls import path

from product.views.product import CreateProductView, ProductView, CreateProduct, UpdateProduct
from product.views.variant import VariantView, VariantCreateView, VariantEditView

app_name = "product"



urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/view/', CreateProductView.as_view(), name='create.product'),
    path('create/', CreateProduct.as_view(), name='createproduct'),
    path('list/', ProductView.as_view(), name='list.product'),
    path('edit/<int:pk>/', UpdateProduct.as_view(), name='edit.product'),
]

