from itertools import product
from tabnanny import verbose
from tkinter import CASCADE

from django.db import models
from django.shortcuts import resolve_url as r


# Create your models here.
class Category(models.Model):
    name = models.CharField('nome', max_length=100, blank=True)
    slug = models.SlugField('slug')
    imageUrl = models.CharField('image', max_length=255)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save()

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Product(models.Model):
    name = models.CharField('nome', max_length=255, blank=True)
    slug = models.SlugField('slug')
    description = models.TextField('descrição')
    basePrice = models.DecimalField('preço base', max_digits=7, decimal_places=2)
    categoryId = models.ForeignKey('Category', verbose_name='categoria', on_delete=models.CASCADE)
    discountPercentage = models.IntegerField('desconto')

    
    class Meta:
        verbose_name='produto'
        verbose_name_plural='produtos'

    def __str__(self):
        self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save()
    
    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
    
    def totalPrice(self):
        if self.discountPercentage > 0:
            self.total_price = (self.basePrice - (self.basePrice * (self.discountPercentage/100)))
        return self.total_price
    

class ImageProduct(models.Model):
    imageUrl = models.TextField('image')
    product = models.ForeignKey('Product', verbose_name='produto', on_delete=models.CASCADE)
