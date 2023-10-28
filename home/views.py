from django.shortcuts import render

from .models import Category


# Create your views here.
def index(request):
    context = {
        "categories": Category.objects.all()
        }
    return render(request, 'index.html', context)