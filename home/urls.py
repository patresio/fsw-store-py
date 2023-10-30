from django.urls import path

from .views import category, index

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('category/', category, name='categoria')
]