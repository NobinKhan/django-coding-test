from django.db.models import Q
from django.views.generic import TemplateView, ListView

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from product.error import get_object_or_None
from product.models import Variant, Product, ProductImage, ProductVariant, ProductVariantPrice



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


class CreateProduct(APIView):

    def post(self, request, formate=None):
        data = request.data
        
        # product data
        product = data.pop('product')
        productSZ = Product(**product)
        try:
            productSZ.clean()
        except Exception as msg :
            return Response({"error":msg.args[0]}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        # image data
        productImage = data.pop('product_image')
        productImageSZ = ProductImage(file_path=productImage, thumbnail=1, product=productSZ)
        try:
            productImageSZ.clean()
        except Exception as msg :
            return Response({"error":msg.args[0]}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        # varients data
        if data.get('product_variants'):
            for pv in data.get('product_variants'):
                pv_one = pv.get('product_variant_one')
                if pv_one:
                    varient = get_object_or_None(Variant, title=pv_one.get('variant'))
                    if not varient:
                        return Response({"error":"varient object not found"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                    pv_one = ProductVariant(
                        variant_title = pv_one.get('variant_title'),
                        variant = varient,
                        product = productSZ
                    )
                
                pv_two = pv.get('product_variant_two')
                if pv_two:
                    varient = get_object_or_None(Variant, title=pv_two.get('variant'))
                    if not varient:
                        return Response({"error":"varient object not found"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                    pv_two = ProductVariant(
                        variant_title = pv_two.get('variant_title'),
                        variant = varient,
                        product = productSZ
                    )
                
                pv_three = pv.get('product_variant_three')
                if pv_three:
                    varient = get_object_or_None(Variant, title=pv_three.get('variant'))
                    if not varient:
                        return Response({"error":"varient object not found"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                    pv_three = ProductVariant(
                        variant_title = pv_three.get('variant_title'),
                        variant = varient,
                        product = productSZ
                    )
                
                price = pv.get('price')
                stock = pv.get('stock')
                try:
                    price = int(price)
                    stock = int(stock)
                except:
                    return Response({"error":"Inavlid price or stock data, only int value acceptable"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                
                product_varient_price = ProductVariantPrice(
                    product_variant_one = pv_one,
                    product_variant_two = pv_two,
                    product_variant_three = pv_three,
                    product = productSZ,
                    price = price,
                    stock = stock
                )
                try:
                    product_varient_price.clean()
                except Exception as msg :
                    return Response({"error":msg.args[0]}, status=status.HTTP_406_NOT_ACCEPTABLE)
                
                try:
                    productSZ.save()
                    productImageSZ.save()
                    if pv_one:
                        pv_one.save()
                    if pv_two:
                        pv_two.save()
                    if pv_three:
                        pv_three.save()
                    product_varient_price.save()
                except Exception as msg :
                    return Response({"error":msg.args[0]}, status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return Response({"error":"Inavlid Product Varient data"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        return Response({"error":"Successfully created"}, status=status.HTTP_201_CREATED)


class UpdateProduct(APIView):

    def post(self, request, pk):
        # validity check
        product = get_object_or_None(Product, pk=pk)
        if not product:
            return Response({"error":"product not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data

        # product data update
        productData = data.pop('product')
        if productData:
            product.title = productData.get('title')
            product.sku = productData.get('sku')
            product.description = productData.get('description')
            try:
                product.clean()
                product.save()
            except Exception as msg :
                return Response({"error":msg.args[0]}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # price and stock data update
        if data.get('product_variants_price'):
            for pvp in data.get('product_variants_price'):
                obj = get_object_or_None(ProductVariantPrice, pk=pvp.get('pk'), product=product)
                if not obj:
                    return Response({"error":"Inavlid product_variants_price data, Object not found"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                price = pvp.get('price')
                stock = pvp.get('stock')
                try:
                    price = int(price)
                    stock = int(stock)
                except:
                    return Response({"error":"Inavlid price or stock data, only int value acceptable"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                

                obj.price = price
                obj.stock = stock
                try:
                    obj.clean()
                    obj.save()
                except Exception as msg :
                    return Response({"error":msg.args[0]}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(f"Successfully Updated {pk}", status=status.HTTP_201_CREATED)

