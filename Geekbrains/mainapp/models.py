from django.db import models
from django.urls import reverse


class Catalog(models.Model):
    name = models.CharField(db_index=True, max_length=200, primary_key=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True)
    seo_descr = models.TextField(blank=True, verbose_name='Описание', max_length=300)
    code = 'catalog'
    image = models.ImageField(upload_to = 'media/', blank=True, verbose_name='Preview')
    available = models.BooleanField(default=True, verbose_name='Доступность')
    class Meta:
        ordering = ['name']
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return self.slug
    def get_absolute_url(self):
        return reverse('mainapp:Choose', args=[self.code, self.slug])

class Subcat(models.Model):
    name = models.CharField(db_index=True, max_length=200, primary_key=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True)
    code = 'categories'
    available = models.BooleanField(default=True, verbose_name='Доступность')
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'media/', blank=True, verbose_name='Изображение категории')
    seo_descr = models.TextField(blank=True, verbose_name='Описание', max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.slug
    def get_absolute_url(self):
        return reverse('mainapp:Choose', args=[self.code, self.slug])

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Subcat, on_delete=models.CASCADE)
    available = models.BooleanField(default=True, verbose_name='Доступность')
    code = 'product'
    image = models.ImageField(upload_to = 'media/', blank=True, verbose_name='Изображение товара')
    seo_descr = models.TextField(blank=True, verbose_name='Описание', max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:Choose', args=[self.code, self.slug])