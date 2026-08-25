from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from shop.models import Category



class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='URL')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    category=models.ForeignKey(
    Category,
    null=True,
    blank=True,
    on_delete=models.CASCADE, #Если категорию удалят - товары тоже удалятся
    related_name='products', #Обратная связь: category.products.all()
    verbose_name='Категория')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

class Category(models.Model):
    category = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories',
        verbose_name='Родительская категория'
    )

