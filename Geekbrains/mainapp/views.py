from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Catalog, Subcat, Product

# Create your views here.


def Choose(request, code, slug_id):
    if code=='catalog':
        return catalog(request, slug_id)
    elif code=='categories':
        return subcat(request, slug_id)
    elif code=='product':
        return product(request, slug_id)
    else:
        return render(request, '/index')

# на главной странице мы должны видеть все каталоги
def main(request):
    full_catalog = Catalog.objects.all()
    context = {'full_catalog': full_catalog}
    return render(request, 'mainapp/index.html', context)



def catalog(request, slug_id=None):
    if len(slug_id) < 1:
        return main(request)
# эта функция каталога должна возвращать все существующие каталоги на индексную страницу
# при запросе конкретного каталога отображать входящие в него категории
    category = None
    full_catalog = Catalog.objects.all()
# выкинем из списка отображаемых категорий те, что могут отключить
    somecatalog = Subcat.objects.filter(available=True)

# дополнительная информация (тест)
    sadd = Catalog.slug
    seo = Catalog.seo_descr
# если каталог выбран - получаем объект и фильтруем категории по этому объекту в поле категория, как подчиненные поля)
    if slug_id:
        category = get_object_or_404(Catalog, slug = slug_id)
        somecatalog = somecatalog.filter(category = category)
    return render(request, 'mainapp/category.html', {
        'category' : category,
        'full_catalog': full_catalog,
        'somecatalog':  somecatalog,
        'sadd' : sadd,
        'seo' : seo
    }
    )

def subcat(request, slug_id=None):
#    category - None
    full_catalog = Subcat.objects.all()
    somecatalog = Product.objects.filter(available=True)
    seo = Subcat.seo_descr
    if slug_id:
        category = get_object_or_404(Subcat, slug = slug_id)
        somecatalog = somecatalog.filter(category = category)
    return render(request, 'mainapp/category.html', {
        'category' : category,
        'full_catalog' : full_catalog,
        'somecatalog' : somecatalog,
        'seo' : seo
    })

def product(request, slug_id):
    products = get_object_or_404(Product, slug=slug_id, available=True)
    return render(request, 'mainapp/products.html', {'product': products
    })



def contacts(request):
    context_c = {'form': {'Address: Russia, N-Tagil city', 'Street: Lenina', 'e-mail: pochta@mail.ru',
                          'phone: 89900000001',
                          }}
    return render(request, 'mainapp/contacts.html', context_c)


def common(request):
    return render(request, 'common/index.html')