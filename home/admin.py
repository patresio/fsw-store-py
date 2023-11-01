from django.contrib import admin

from home.models import Category, ImageProduct, Product

# Register your models here.

class ImageProductInline(admin.TabularInline):
    model = ImageProduct
    extra = 1

class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ImageProductInline]

admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category)