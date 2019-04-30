"""Geekbrains URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', include('mainapp.urls', namespace='mainapp')),
    url(r'^', include(('mainapp.urls', 'mainapp'), namespace='mainapp')),
    path('', mainapp.main, name='main_page'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('common/', mainapp.common, name='common'),
#    url(r'', mainapp.main),
#    url(r'^products', mainapp.products),
#    url(r'^contacts', mainapp.contacts),
#    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
