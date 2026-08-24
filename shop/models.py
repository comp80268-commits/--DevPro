from django.db import models
from app.models import *


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название: shop')
    slug = models.SlugField(max_length=200, verbose_name='URL: shop')
    image = models.ImageField(verbose_name='Икока категории')


    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

        def __str__(self):
            return self.name


class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField(max_length=200, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    stock = models.BooleanField(default=True, verbose_name='Наличие')
    product = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Продукт'
    )


