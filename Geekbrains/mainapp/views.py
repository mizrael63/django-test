from django.shortcuts import render

# Create your views here.

def main(request):
    context = {'user': {'name': 'иван'}, 'array' : [1,2,3,4,5]}
    return render(request, 'mainapp/index.html', context)

def products(request):
    return render(request, 'mainapp/products.html')

def contacts(request):
    context_c = {'form': {'Address: Russia, N-Tagil city', 'Street: Lenina', 'e-mail: pochta@mail.ru',
                          'phone: 89900000001',
                          }}
    return render(request, 'mainapp/contacts.html', context_c)

def common(request):
    return render(request, 'common/index.html')