from django.contrib import admin
from .models import Catalog, Product, Subcat



class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'code', 'available',  'seo_descr']
    prepopulated_fields = {'slug': ('name', )}
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'available', 'code', 'seo_descr', 'image']
    list_filter = ['category', 'available']
    prepopulated_fields = {'slug': ('name', )}
class SubcatAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'available', 'code', 'seo_descr', 'image']
    list_filter = ['category', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Subcat, SubcatAdmin)
