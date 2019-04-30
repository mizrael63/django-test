from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.main),
    url(r'^(?P<code>[-\w]+)/(?P<slug_id>[-\w]+)/$', views.Choose, name='Choose'),
    path('product/', views.catalog, name='products'),
#    path('contacts/', mainapp.contacts, name='contacts'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)