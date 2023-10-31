from django.shortcuts import render

from home.models import Category

# Create your views here.

def catalog(request):
    context = {
        "categories": Category.objects.all()
        }
    return render(request, 'catalog/catalog.html', context)