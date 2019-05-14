from django.core.management.base import BaseCommand
from mainapp.models import Catalog, Subcat, Product
from django.contrib.auth.models import User
from authnapp.models import ShopUser

import json, os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Catalog.objects.all().delete()
        for category in categories:
            new_category = Catalog(**category)
            new_category.save()

        products = load_from_json('products')

        Subcat.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = Catalog.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Subcat(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
 #       super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)