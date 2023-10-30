from django.shortcuts import render

from .models import Category, ImageProduct, Product


# Create your views here.
def index(request):
    context = {
        "categories": Category.objects.all(),
        "products": Product.objects.all(),
        "images": ImageProduct.objects.all(),
        "keyboards": Product.objects.filter(categoryId=2),
        "mouses": Product.objects.filter(categoryId=1)
        }
    return render(request, 'index.html', context)