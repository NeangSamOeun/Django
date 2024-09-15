from django.contrib import admin
from shop.models import product
from shop.models import Category


admin.site.register(product)
admin.site.register(Category)