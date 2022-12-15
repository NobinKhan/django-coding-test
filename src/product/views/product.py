from django.views.generic import TemplateView, ListView

from product.models import Variant, Product


class CreateProductView(TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductView(ListView):
    template_name = 'products/list.html'
    # context_object_name = 'data'
    paginate_by = 2

    def get_queryset(self):
        print("\n\n triger \n\n")
        return Product.objects.all().prefetch_related('ProductVariantPrice')

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductView, self).get_context_data(*args, **kwargs)
    #     context['products'] = self.queryset
    #     return context