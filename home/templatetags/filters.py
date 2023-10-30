from atexit import register

from django import template

from home.models import Category, ImageProduct, Product

register = template.Library()


@register.filter(name='get_first_image')
def get_first_image(product):
    if image := ImageProduct.objects.filter(product=product).first():
        return image.imageUrl
    else:
        return False
    

@register.filter(name='get_category')
def get_category(products, category):
    categoryId = Category.objects.filter(slug=category)
    if products := Product.objects.filter(categoryId=categoryId):
        return products