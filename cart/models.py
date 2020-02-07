from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed

from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.000, max_digits=100, decimal_places=3)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for product in products:
            total += product.price

        instance.total = total
        instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)
