# Generated by Django 2.1.7 on 2019-04-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190430_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='subcat',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Изображение категории'),
        ),
    ]