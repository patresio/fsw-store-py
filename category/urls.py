from django.urls import path

from .views import catalog

app_name = 'categories'

urlpatterns = [
    path('', catalog, name='catalog'),
]