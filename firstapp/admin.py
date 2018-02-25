from django.contrib import admin

# Register your models here.

from firstapp.models import Product
admin.site.register(Product)
#admin.site.register(ShopCart)
