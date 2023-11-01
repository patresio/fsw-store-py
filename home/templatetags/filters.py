from atexit import register

from django import template

from home.models import ImageProduct

register = template.Library()


@register.filter(name='get_first_image')
def get_first_image(product):
    if image := ImageProduct.objects.filter(product=product).first():
        return image.imageUrl
    else:
        return False
    