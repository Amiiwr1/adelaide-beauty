from django.contrib import admin
from .models import Cart


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'updated', 'created')
    list_filter = ('user',)
    ordering = ('-created',)
    search_fields = ('user',)
    date_hierarchy = 'created'
