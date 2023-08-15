from django.contrib import admin
from .models import Product, Offer

# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)