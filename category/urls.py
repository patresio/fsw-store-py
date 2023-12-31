from django.urls import path

from .views import catalog, category, offers, product

app_name = 'categories'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('offers/', offers, name='offers'),
    path('<slug:slug>/', category, name='category'),
    path('<slug:slug2>/<slug:slug1>/', product, name='product'),
]