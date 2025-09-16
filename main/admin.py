from django.contrib import admin
from .models import Product
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'description', 'get_category_display', 'is_featured', 'item_views', 'release_year', 'thumbnail_preview')

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.thumbnail)
        return "No Image"

    thumbnail_preview.short_description = 'Thumbnail'

# Register your models here.
admin.site.register(Product, ProductAdmin)
