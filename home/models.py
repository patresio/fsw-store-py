from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('name', max_length=100, blank=True)
    slug = models.SlugField('slug')
    imageUrl = models.CharField('image', max_length=255)
