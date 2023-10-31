from django.urls import path

from .views import catalog, category

app_name = 'categories'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('<slug:slug>/', category, name='category'),
]