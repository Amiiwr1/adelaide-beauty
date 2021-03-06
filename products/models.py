import random
import os

from django.db import models
from django.urls import reverse
from users.models import CustomUser


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Category(models.Model):
    CAT_CHOICES = [
        ('eyelash', 'Eyelash'),
        ('eyebrow lash', 'Eyebrow lash'),
        ('lipstick', 'Lipstick'),
        ('powder', 'Powder'),
    ]
    category = models.CharField(max_length=10, choices=CAT_CHOICES)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.CharField(max_length=120, default='title', null=False, blank=False)
    brand = models.CharField(max_length=120, default='brand', null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True)
    slug = models.SlugField(blank=False, unique=True, null=False)
    description = models.TextField(null=True, default='description')
    short_description = models.TextField(null=True, default='s-desc', max_length=120)
    pros = models.TextField(null=True, default='pros')
    cons = models.TextField(null=True, default='cons')
    old_price = models.DecimalField(decimal_places=3, max_digits=20, default=0.000)
    price = models.DecimalField(decimal_places=3, max_digits=20, default=0.000)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    sale = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    @property
    def approved_comments(self):
        return self.comments.filter(is_approved=True)


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=620, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s comment for product %s" % (self.author.username, self.product.title)
