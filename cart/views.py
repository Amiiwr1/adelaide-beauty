from django.contrib.auth.models import User
from django.http import Http404

from django.urls import reverse
from django.views import generic

from cart.models import Cart
from products.models import Product


class CartDetail(generic.DetailView):
    template_name = 'cart/cart_detail.html'
    model = Cart

    def get_object(self, queryset=None):
        if User.objects.filter(id=self.request.user.id).exists():
            user = User.objects.filter(id=self.request.user.id).get()
            cart, created = Cart.objects.get_or_create(defaults={"user": user}, user=user)
            return cart
        raise Http404


class CartUpdate(generic.UpdateView):
    template_name = 'cart/update-cart.html'
    model = Cart
    fields = ('products',)

    def post(self, request, *args, **kwargs):
        cart, created = Cart.objects.update_or_create(defaults={"user": self.request.user}, user=self.request.user)
        product_id = request.POST.get("product_id")
        if Product.objects.get(id=product_id):
            product = Product.objects.get(id=product_id)
            if product in cart.products.all():
                cart.products.remove(product)
                cart.save()
            else:
                cart.products.add(product)
                cart.save()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            return self.form_invalid(form)
        raise Http404

    def get_success_url(self):
        return reverse('cart:detail')
