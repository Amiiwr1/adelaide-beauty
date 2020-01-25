from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 50
    template_name = 'products/product-list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
