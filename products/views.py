from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 50
    template_name = 'products/product-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data(object_list=None, **kwargs)
        context.update(
            {
                "new_arrival": Product.objects.filter(is_new=True),
                "sales": Product.objects.filter(sale=True),
                "populars": Product.objects.filter(popular=True)
            }
        )
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
