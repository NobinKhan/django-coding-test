from django.views.generic import TemplateView, ListView
from django.db.models import Q
from product.models import Variant, Product


class CreateProductView(TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.all().values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductView(ListView):
    template_name = 'products/list.html'
    paginate_by = 2

    def get_queryset(self):
        productTitle = self.request.GET.get('title')
        productvariant = self.request.GET.get('variant')
        price_from = self.request.GET.get('price_from')
        price_to = self.request.GET.get('price_to')
        date = self.request.GET.get('date')

        qs = Product.objects.prefetch_related('ProductVariantPrice')
        if productTitle:
            qs = qs.filter(Q(title__contains=productTitle))
        if productvariant:
            qs = qs.filter(
                Q(ProductVariantPrice__product_variant_one__variant_title=productvariant) |
                Q(ProductVariantPrice__product_variant_two__variant_title=productvariant) |
                Q(ProductVariantPrice__product_variant_three__variant_title=productvariant)
            )
        if price_from and price_to:
            qs = qs.filter(Q(ProductVariantPrice__price__range=(price_from, price_to)))
        if date:
            qs = qs.filter(Q(created_at__contains=date) | Q(updated_at__contains=date))
        return qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['varients'] = Variant.objects.prefetch_related('productvariant_set').distinct()
        return context

