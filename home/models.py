from tabnanny import verbose

from django.db import models
from django.shortcuts import resolve_url as r


# Create your models here.
class Category(models.Model):
    name = models.CharField('name', max_length=100, blank=True)
    slug = models.SlugField('slug')
    imageUrl = models.CharField('image', max_length=255)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
