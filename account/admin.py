from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)


# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(ShippingAddress)
