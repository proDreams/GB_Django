from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'customer', 'total_price', 'ordered_at',
    list_filter = 'customer',


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title', 'image_preview', 'price', 'count', 'added_at',
    exclude = 'added_at',

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="%s" width="100"/>' % obj.image.url)
        else:
            return '(No image found)'

    image_preview.allow_tags = True


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'email', 'phone', 'registered_at',
    exclude = 'registered_at',
