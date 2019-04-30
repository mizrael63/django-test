# Generated by Django 2.1.7 on 2019-04-30 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('name', models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=200)),
                ('seo_descr', models.TextField(blank=True, max_length=300, verbose_name='SEO описание')),
                ('image', models.ImageField(blank=True, upload_to='static/img/category/%Y%/%m/%d/', verbose_name='Preview')),
                ('available', models.BooleanField(default=True, verbose_name='Доступность')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('available', models.BooleanField(default=True, verbose_name='Доступность')),
                ('image', models.ImageField(blank=True, upload_to='static/img/products/%Y%/%m/%d/', verbose_name='Изображение категории')),
                ('seo_descr', models.TextField(blank=True, max_length=200, verbose_name='SEO описание')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subcat',
            fields=[
                ('name', models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=200)),
                ('available', models.BooleanField(default=True, verbose_name='Доступность')),
                ('image', models.ImageField(blank=True, upload_to='static/img/category/%Y%/%m/%d/', verbose_name='Изображение категории')),
                ('seo_descr', models.TextField(blank=True, max_length=200, verbose_name='SEO описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Catalog')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Subcat'),
        ),
    ]