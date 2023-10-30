from django.shortcuts import render

from .models import Category, ImageProduct, Product


# Create your views here.
def index(request):
    context = {
        "categories": Category.objects.all(),
        "products": Product.objects.all(),
        "images": ImageProduct.objects.all()
        }
    return render(request, 'index.html', context)