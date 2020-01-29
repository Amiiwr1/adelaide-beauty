from django.contrib import admin
from .models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'price', 'created')
    list_filter = ('title', 'price', 'is_new', 'popular', 'sale')
    ordering = ('-created',)
    search_fields = ('title',)
    date_hierarchy = 'created'
    sortable_by = ('title', 'created')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
