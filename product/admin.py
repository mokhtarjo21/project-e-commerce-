
from django.contrib import admin
from .models import Product,category,cart
# Register your models here.
admin.site.register(category)
admin.site.register(Product)
admin.site.register(cart)
