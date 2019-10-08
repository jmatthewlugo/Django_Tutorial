from django.contrib import admin
from django.db import models
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','prince','stock')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)