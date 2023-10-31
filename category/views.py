from django.shortcuts import get_object_or_404, render

from home.models import Category, ImageProduct, Product

# Create your views here.

def catalog(request):
    context = {
        "categories": Category.objects.all()
        }
    return render(request, 'catalog/catalog.html', context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        "category": category,
        "products": Product.objects.filter(categoryId=category.id).all(),
    }
    return render(request, 'category/category.html', context)

def product(request, slug1, slug2):
    product = get_object_or_404(Product, slug=slug1)
    context = {
        "product": product,
        "images": ImageProduct.objects.filter(product=product.id).all()
    }
    return render(request, 'product/products.html', context)